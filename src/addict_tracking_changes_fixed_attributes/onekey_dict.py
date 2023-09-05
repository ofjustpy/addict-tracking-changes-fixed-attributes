"""
A tracking dict that contains only one key.
Its used by ofjustpy as an optimized
enhancement for Dict which  track only on
attribute typically classes attribute.
"""

class OneKeyDict(dict):
    def __init__(__self, tracked_key, *args,  **kwargs):
        object.__setattr__(__self, "__tracked_key", tracked_key)
        object.__setattr__(__self, "__change_state", False)
        
        pass

    def __setattr__(self, name, value):
        #print("in __setattr__", name, " ", value)
        self[name] = value

    def __setitem__(self, name, value):
        #print(f"in __setitem__ for {name}")
        assert name == object.__getattribute__(self, "__tracked_key")
        object.__setattr__(self, "__change_state", True)
        super(OneKeyDict, self).__setitem__(name, value)



    def __getattr__(self, item):

        child_item = super(OneKeyDict, self).__getitem__(item)

        return child_item
        

    def __getitem__(self, key):
        return self.__getattr__(key)

    # def __getattribute__(self, name):
    #     raise AttributeError(f"'mydict' object has no attribute '{name}'")
    
    def __missing__(self, name):
        print (f"__missing__ called with name = {name} ")
        raise ValueError("do not go via missing rout")

    def __delitem__(self, key):
        return super(OneKeyDict, self).__delitem__(key)

    def __delattr__(self, name):
        del self[name]

    def to_dict(self):
        assert False

    def __copy__(self):
        raise NotImplementedError("Shallow copy is not supported for this class.")

    def __deepcopy__(self, memo):
        assert False

    def freeze(self, shouldFreeze=True):
        assert False

    def unfreeze(self):
        assert False

    def has_changed_history(self):
        return object.__getattribute__(self, "__change_state")

    def get_changed_history(self, prefix="", path_guards=None):
        if object.__getattribute__(self, "__change_state"):
            yield "/" + object.__getattribute__(self, "__tracked_key")
        

                
            
        
    def clear_changed_history(self):
        object.__setattr__(self, "__change_state", False)

    def set_tracker(self, track_changes=False):
        """
        pickle/unpickle forgets about trackers and frozenness
        """
        assert False




