def list_check(lst):
    """Are all items in lst a list?

        >>> list_check([[1], [2, 3]])
        True

        >>> list_check([[1], "nope"])
        False
    """
    # Use all() with isinstance to check if every element is a list
    return all(isinstance(item, list) for item in lst)
    # Time complexity: O(n), where n is the length of lst
    # Space complexity: O(1), only a generator is used
