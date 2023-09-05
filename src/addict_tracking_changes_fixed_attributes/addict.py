# This file is part of addict-tracking-changes
#
# Copyright (c) [2023] by Webworks, MonalLabs.
# This file is released under the MIT License.
#
# Author(s): Webworks, Monal Labs.
# MIT License
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
import copy
import sys
import traceback
from collections import UserList


# This code is not yet ready
# 90% of dicts in ofjustpy is zero-key dict and one-key Dict.
# Hence we don't really need dicts with > 1 keys. 

class Dict(dict):
    def __init__(__self, tracked_keys, *args, sig_size = 2, **kwargs):

        # Strategy: we maintain a list of signatures
        # for given list of tracked keys

        # Signature for a tracked key is derived
        # as first __sig_size letter

        assert len(tracked_keys) > 0

        # build the tracked_keys_sig vector
        object.__setattr__(__self, "__sig_size", sig_size)
        tracked_keys_sig_vec = ['c']

        # a corresponding vector to maintain/track the changes of the tracked keys
        object.__setattr__(__self, "__change_state_vec", [False])
        
        pass

    def __setattr__(self, name, value):
        change_state_vec = object.__getattribute__(self, "__change_state_vec"
                                                   )
        if change_state_vec is None:
            assert False
            
        tracked_keys = ['classes']
        tracked_keys_sig_vec = ['c']
        sig_size = object.__getattribute__(self, "__sig_size")
        
        try:
            # Find the index where the key occurs
            index = tracked_keys_sig_vec.index(name[0:sig_size])
            change_state_vec[index] = True
        except ValueError:
            # name is not being tracked
            pass
        

        self[name] = value

    def __setitem__(self, name, value):
        print ("__setitem__ called")
        super(Dict, self).__setitem__(name, value)



    def __getattr__(self, item):
        child_item = super(Dict, self).__getitem__(item)

        return child_item

    def __getitem__(self, key):
        return self.__getattr__(key)

    def __missing__(self, name):
        if object.__getattribute__(self, "__frozen"):
            raise KeyError(name)
        return self.__class__(
            __key=name,
        )

    def __delitem__(self, key):
        return super(Dict, self).__delitem__(key)

    def __delattr__(self, name):
        del self[name]

    def to_dict(self):
        base = {}
        for key, value in self.items():
            if isinstance(value, type(self)):
                base[key] = value.to_dict()
            elif isinstance(value, (list, tuple)):
                base[key] = type(value)(
                    item.to_dict() if isinstance(item, type(self)) else item
                    for item in value
                )
            else:
                base[key] = value
        return base

    def __copy__(self):
        raise NotImplementedError("Shallow copy is not supported for this class.")

    def __deepcopy__(self, memo):
        other = self.__class__()
        memo[id(self)] = other
        for key, value in self.items():
            other[copy.deepcopy(key, memo)] = copy.deepcopy(value, memo)
        return other

    def freeze(self, shouldFreeze=True):
        object.__setattr__(self, "__frozen", shouldFreeze)
        for _key, val in self.items():
            if isinstance(val, Dict):
                val.freeze(shouldFreeze)

    def unfreeze(self):
        self.freeze(False)

    def has_changed_history(self):
        assert False
        return False

    def get_changed_history(self, prefix="", path_guards=None):
        change_state_vec = object.__getattribute__(self, "__change_state_vec"
                                                   )
        tracked_keys = ['classes']
        tracked_keys_sig_vec = ['c']
        change_state_vec = object.__getattribute__(self, "__change_state_vec"
                                                   )
        
        for tk, tv in zip(tracked_keys, change_state_vec):
            if tv:
                yield tk
                
            
        
    def clear_changed_history(self):
        change_state_vec = object.__getattribute__(self, "__change_state_vec"
                                                   )
        
        for i in range(len(change_state_vec)):
            change_state_vec[i] = False

    def set_tracker(self, track_changes=False):
        """
        pickle/unpickle forgets about trackers and frozenness
        """
        assert False




