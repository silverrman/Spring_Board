def partition(lst, fn):
    """Partition lst by predicate.
     
     - lst: list of items
     - fn: function that returns True or False
     
     Returns new list: [a, b], where `a` are items that passed fn test,
     and `b` are items that failed fn test.

        >>> def is_even(num):
        ...     return num % 2 == 0
        
        >>> def is_string(el):
        ...     return isinstance(el, str)
        
        >>> partition([1, 2, 3, 4], is_even)
        [[2, 4], [1, 3]]
        
        >>> partition(["hi", None, 6, "bye"], is_string)
        [['hi', 'bye'], [None, 6]]
    """
    # Initialize two lists: one for items passing the predicate, one for failing
    passed = []
    failed = []
    
    # Iterate through each item in the list
    for item in lst:
        if fn(item):
            passed.append(item)  # Item passed the predicate
        else:
            failed.append(item)  # Item failed the predicate
    
    # Return a list containing both lists
    return [passed, failed]
    
    # Time complexity: O(n), where n is the length of lst
    # Space complexity: O(n), for storing the partitioned lists