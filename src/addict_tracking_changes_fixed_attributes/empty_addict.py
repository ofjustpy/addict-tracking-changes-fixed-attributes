"""
A tracking dict that contains no keys.
Its used by ofjustpy as an optimized
enhancement for Dict which do not track any
attributes
"""

class EmptyDict(dict):
    def __init__(__self,  *args,  **kwargs):
        
        pass

    def __setattr__(self, name, value):
        assert False

    def __setitem__(self, name, value):
        assert False

    def __getattr__(self, item):
        assert False


    def __getitem__(self, key):
        assert False

    def __missing__(self, name):
        assert False

    def __delitem__(self, key):
        assert False

    def __delattr__(self, name):
        assert False

    def to_dict(self):
        assert False

    def __copy__(self):
        raise NotImplementedError("Shallow copy is not supported for this class.")

    def __deepcopy__(self, memo):
        assert False


    def has_changed_history(self):
        return False

    def get_changed_history(self, prefix="", path_guards=None):
        pass
                
            
        
    def clear_changed_history(self):
        pass

    def set_tracker(self, track_changes=False):
        """
        pickle/unpickle forgets about trackers and frozenness
        """
        assert False




