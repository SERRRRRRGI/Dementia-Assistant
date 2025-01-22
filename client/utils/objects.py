from collections.abc import Iterable

def get_subscriptable(obj, key, default=None):
    # Check if the object is a dictionary and use the get() method
    if isinstance(obj, dict):
        return obj.get(key, default)
    
    # Check if the object is iterable and not a string (which is iterable but should not be treated like a collection)
    if isinstance(obj, Iterable) and not isinstance(obj, (str, bytes)):
        try:
            return obj[key]  # Attempt to access the element by key (index)
        except (IndexError, TypeError, KeyError):
            return default  # If key is invalid, return default
    else:
        # If object is not subscriptable, return default if key != 0, else wrap it in a list and return the object
        if key == 0:
            return obj
        return default