def two_list_dictionary(keys, values):
    """Return dict mapping keys to values.

    If there are not enough values, use None for missing values.
    If there are too many values, ignore extras.

    >>> two_list_dictionary(['a', 'b', 'c'], [1, 2, 3])
    {'a': 1, 'b': 2, 'c': 3}
    >>> two_list_dictionary(['a', 'b', 'c'], [1, 2])
    {'a': 1, 'b': 2, 'c': None}
    >>> two_list_dictionary(['a', 'b'], [1, 2, 3])
    {'a': 1, 'b': 2}
    """
    # Use zip to pair keys and values, and dict to build the dictionary
    out = {k: v for k, v in zip(keys, values)}
    # If there are more keys than values, fill with None
    for k in keys[len(values):]:
        out[k] = None
    return out
    # Time complexity: O(n), where n is the number of keys
    # Space complexity: O(n), for the new dictionary
    """Given keys and values, make dictionary of those.
    
        >>> two_list_dictionary(['x', 'y', 'z'], [9, 8, 7])
        {'x': 9, 'y': 8, 'z': 7}
        
    If there are fewer values than keys, remaining keys should have value
    of None:
    
        >>> two_list_dictionary(['a', 'b', 'c', 'd'], [1, 2, 3])
        {'a': 1, 'b': 2, 'c': 3, 'd': None}
    
    If there are fewer keys, ignore remaining values:

        >>> two_list_dictionary(['a', 'b', 'c'], [1, 2, 3, 4])
        {'a': 1, 'b': 2, 'c': 3}
   """