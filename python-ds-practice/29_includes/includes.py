def includes(collection, sought, start=None):
    """Is sought in collection, starting at index start?

    >>> includes([1, 2, 3], 1)
    True
    >>> includes([1, 2, 3], 1, 2)
    False
    >>> includes("hello", "e")
    True
    >>> includes((1, 2, 3), 3)
    True
    >>> includes({1, 2, 3}, 1)
    True
    >>> includes({"a": 1, "b": 2}, "b")
    True
    """
    # For sequences (list, tuple, str), use slicing if start is given
    if isinstance(collection, (list, tuple, str)):
        if start is not None:
            return sought in collection[start:]
        return sought in collection
    # For sets, just check membership
    elif isinstance(collection, set):
        return sought in collection
    # For dicts, check keys
    elif isinstance(collection, dict):
        return sought in collection.keys()
    return False
    # Time complexity: O(n) in general
    # Space complexity: O(1)
    """Is sought in collection, starting at index start?

    Return True/False if sought is in the given collection:
    - lists/strings/sets/tuples: returns True/False if sought present
    - dictionaries: return True/False if *value* of sought in dictionary

    If string/list/tuple and `start` is provided, starts searching only at that
    index. This `start` is ignored for sets/dictionaries, since they aren't
    ordered.

        >>> includes([1, 2, 3], 1)
        True

        >>> includes([1, 2, 3], 1, 2)
        False

        >>> includes("hello", "o")
        True

        >>> includes(('Elmo', 5, 'red'), 'red', 1)
        True

        >>> includes({1, 2, 3}, 1)
        True

        >>> includes({1, 2, 3}, 1, 3)  # "start" ignored for sets!
        True

        >>> includes({"apple": "red", "berry": "blue"}, "blue")
        True
    """