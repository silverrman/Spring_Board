def sum_floats(nums):
    """Return sum of floating point numbers in nums.
    
        >>> sum_floats([1.5, 2.4, 'awesome', [], 1])
        3.9
        
        >>> sum_floats([1, 2, 3])
        0
    """
    # Use list comprehension and isinstance to filter floats, then sum
    return sum([num for num in nums if isinstance(num, float)])
    # Time complexity: O(n), where n is the length of nums
    # Space complexity: O(n), for the filtered list
