def compact(lst):
    """Return a copy of lst with non-true elements removed.

        >>> compact([0, 1, 2, '', [], False, (), None, 'All done'])
        [1, 2, 'All done']
    """
    # Use list comprehension to filter out non-true (falsy) elements
    # In Python, values like 0, '', [], False, (), None are considered falsy
    # Only truthy values will be included in the result list
    return [item for item in lst if item]
    
    # Time complexity: O(n), where n is the length of lst
    # Space complexity: O(n), for the new list