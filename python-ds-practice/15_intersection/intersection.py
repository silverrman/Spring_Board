def intersection(l1, l2):
    """Return intersection of two lists as a new list::
    
        >>> intersection([1, 2, 3], [2, 3, 4])
        [2, 3]
        
        >>> intersection([1, 2, 3], [1, 2, 3, 4])
        [1, 2, 3]
        
        >>> intersection([1, 2, 3], [3, 4])
        [3]
        
        >>> intersection([1, 2, 3], [4, 5, 6])
        []
    """
    # Convert the second list to a set for O(1) lookup times
    set2 = set(l2)
    # Use list comprehension to filter elements in l1 that are also in l2
    # This preserves the order of elements from l1
    return [item for item in l1 if item in set2]
    
    # Time complexity: O(n + m), where n = len(l1), m = len(l2)
    # Space complexity: O(m), for the set conversion