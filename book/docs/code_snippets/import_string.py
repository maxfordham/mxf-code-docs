# ---
# jupyter:
#   jupytext:
#     formats: py:light
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.13.6
#   kernelspec:
#     display_name: Python [conda env:ipyautoui]
#     language: python
#     name: conda-env-ipyautoui-xpython
# ---

# + [markdown] tags=[]
# # import strings 
#
# the functions defined below can be used to define the import location of a python object as a string.  
# this could be useful to define within a json file, for example, what python object to use to render some json data. (ipyrun and ipyautoui use this functionality.)
#
# __note.__ 
#
# - when using `functool.partial`, the callable object doesn't have a `__name__` attribute so the `obj_to_importstr` method below won't work. 
#     - you can use the `functools.wraps` decorator instead
# - lambda functions have the generic `__name__ == '<lambda>'`
#     - the `__name__` of a lambda function can be explicitly defined
# -

import sys
sys.path.append('/mnt/c/engDev/git_mf/ipyautoui/src')

# +
import importlib.util
import typing

def obj_to_importstr(obj: typing.Callable):
    """
    given a callable callable object this will return the 
    import string to. From the string the object can be 
    initiated again using importlib. This is useful for 
    defining a function or class in a json serializable manner
    
    Args:
        obj: typing.Callable
    Returns: 
        str: import string
        
    Example:
        >>> obj_from_importstr(pathlib.Path)
        'pathlib.Path'
    """
    try:
        mod = obj.__module__
    except:
        raise ValueError(f'{str(obj)} doesnt have a __module__ attribute.')
    try: 
        nm = obj.__name__
    except:
        raise ValueError(f'{str(obj)} doesnt have a __name__ attribute. (might be a functool.partial?)')

    return mod +'.'+ nm

def obj_from_importstr(importstr: str) -> typing.Type:
    """
    given the import string of an object this function and returns the Obj. 
    
    makes it easy to define class used as a string in a json
    object and then use this class to re-initite it.
    
    Args:
        import_string: == obj.__module__ + '.' + obj.__name__
    Returns: 
        obj
        
    Example:
        >>> obj_from_importstr('pathlib.Path')
        pathlib.Path
    """
    mod, nm = importstr.rsplit('.', 1)

    return getattr(importlib.import_module(mod), nm)


# -

# eg
obj_from_importstr('ipyautoui.AutoUi')
