def last_element(lst):
    """Return last item in list (None if list is empty.
    
        >>> last_element([1, 2, 3])
        3
        
        >>> last_element([]) is None
        True
    """
    # Check if the list has any elements
    # In Python, empty collections are considered False in boolean context
    if lst:
        # Return the last element using negative indexing
        # In Python, lst[-1] accesses the last element of the list
        return lst[-1]
    # If the list is empty, return None
    return None
    
    # Time complexity: O(1) - constant time access to the last element
    # Space complexity: O(1) - no additional space needed