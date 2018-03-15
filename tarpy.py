# -*- coding: utf-8 -*-
"""
Created on Thu Mar 15 17:51:00 2018

@author: Tariq Shihadah
"""

#%%


"""
DEPENDENCIES
"""


import time


#%%


"""
OBJECTS
"""


#%% Dx
"""
Dictionary-like object which maintains item order and offers some additional
functionality for dictionaries of objects.
"""


class Dx(object):
    _registry = []
    
    
    """ DUNDER METHODS """
    def __init__(self, *args, name=None, **kwargs):
        # Add new Dx to registry
        self._registry.append(self)
        self._index = len(self._registry) - 1
        
        # Initialize keys/vals lists
        self.items = []
        self.keys = []
        self.vals = []
        
        # Initialize input variables
        self.name = name if not name in [None, ""] else "Dx #{}".format(self._index)
        
        """ Collect input keys/vals """
        # *args
        for arg in args:
            
            # Check for valid key
            if arg[0] in self.keys:
                raise IndexError("Key \"{}\" is invalid or may already be in use (*arg input).".format(arg[0]))
            
            self.items.append((arg[0], arg[1]))
            self.keys.append(arg[0])
            self.vals.append(arg[1])
       
        # **kwargs
        for key, val in kwargs.items():
            
            # Check for valid key
            if key in self.keys:
                raise IndexError("Key \"{}\" is invalid or may already be in use (**kwarg input).".format(key))
            
            self.items.append((key, val))
            self.keys.append(key)
            self.vals.append(val)

    def __repr__(self):
        return "{}: Dictionary-like object which maintains order of items.".format(self.name)
    
    def __str__(self):
        return "{}: Dictionary-like object which maintains order of items.".format(self.name)
    
    def __len__(self):
        return self.length
    
    def __contains__(self, x):
        return x in self.keys
    
    def __getitem__(self, key):
        if not key in self.keys:
            raise IndexError(str(key) + " is not a valid index.")
        return self.vals[self.keys.index(key)]
    
    def __setitem__(self, key, val):

        # Test for availability of key
        if key in self.keys:
            self.vals[self.keys.index(key)] = val
        else:
            self.keys.append(key)
            self.vals.append(val)
            self.items.append((key,val))
    
    def __iter__(self):
        return iter(self.keys)
    
    
    """ OBJECT METHODS """
    def val(self, key):
        """
        Return the value associated with the input key.
        """
        if not key in self.keys:
            raise IndexError(str(key) + " is not a valid index.")
        return self.vals[self.keys.index(key)]

    def key(self, val):
        """
        Return the first instance of the key associated with the input value.
        """
        if not val in self.vals:
            raise IndexError(str(val) + " is not a valid value.")
        return self.keys[self.vals.index(val)]
    
    def add(self, key, val):
        """
        Add the input value at the input key.
        """
        # Test for availability of key
        if key in self.keys:
            raise KeyError(str(key) + " is not an available index.")
        
        # Append new values
        self.keys.append(key)
        self.vals.append(val)
        self.items.append((key,val))
        
    def rem(self, key):
        """
        Remove the input key and its associated value.
        """
        # Test for existence of key
        if key not in self.keys:
            raise KeyError(str(key) + " is not a valid index.")
        
        # Remove key/value
        index = self.keys(key)
        del self.keys[index]
        del self.vals[index]
        
    def sum_attr(self, attr, ignore_errors = False, return_error_count = False):
        """
        Calculate the sum of the indicated attribute on all values
        within the dictionary and return the result.
        """
        result = 0
        error_count = 0
        # Iterate over all values in the dictionary and attempt to sum attributes
        for val in self.vals:
            try:
                result += getattr(val, attr)
            except AttributeError:
                if ignore_errors:
                    error_count += 1
                    continue
                else:
                    raise AttributeError("Input attribute is invalid and may not exist in all dictionary objects.")
            except TypeError:
                if ignore_errors:
                    continue
                    error_count += 1
                else:
                    raise AttributeError("Input attribute cannot be summed.")
                    
        # If errors are being ignored, and the user requests the count of errors, print count
        if ignore_errors and return_error_count:
            print("Total errors encountered:", error_count)
        
        return result
    
    
    """ OBJECT PROPERTIES """
    @property
    def length(self):
        """
        Return the number of key/value pairs.
        """
        return len(self.keys)


#%%
        
    
"""
FUNCTIONS
"""


#%% timmy
"""
Function timing wrapper which prints a standard output message in various formats.
"""


""" DEFAULT: Print Seconds """
def timmy(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print("\n\nPROCEDURE COMPLETE",
              "\n - Procedure execution time: {:.2f} seconds".format(end - start))
        return result
    return wrapper


""" Print Seconds """
def timmy_s(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print("\n\nPROCEDURE COMPLETE",
              "\n - Procedure execution time: {:.2f} seconds".format(end - start))
        return result
    return wrapper


""" Print Miliseconds """
def timmy_ms(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print("\n\nPROCEDURE COMPLETE",
              "\n - Procedure execution time: {:.2f} miliseconds".format((end - start) * 1000))
        return result
    return wrapper


""" Print Minutes """
def timmy_m(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print("\n\nPROCEDURE COMPLETE",
              "\n - Procedure execution time: {:.2f} minutes".format((end - start) / 60))
        return result
    return wrapper


""" Print Hours """
def timmy_h(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print("\n\nPROCEDURE COMPLETE",
              "\n - Procedure execution time: {:.2f} hours".format((end - start) / 3600))
        return result
    return wrapper


#%%


