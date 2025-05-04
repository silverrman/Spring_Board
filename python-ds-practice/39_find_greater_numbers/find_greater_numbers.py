def find_greater_numbers(nums):
    """Return count of number pairs where later number is greater than earlier.

    >>> find_greater_numbers([1, 2, 3])
    3
    >>> find_greater_numbers([6, 1, 2, 7])
    4
    >>> find_greater_numbers([5, 4, 3, 2, 1])
    0
    """
    count = 0
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n):
            if nums[j] > nums[i]:
                count += 1
    return count
    # Time complexity: O(n^2), where n is the length of nums
    # Space complexity: O(1)
    """Return # of times a number is followed by a greater number.

    For example, for [1, 2, 3], the answer is 3:
    - the 1 is followed by the 2 *and* the 3
    - the 2 is followed by the 3

    Examples:

        >>> find_greater_numbers([1, 2, 3])
        3

        >>> find_greater_numbers([6, 1, 2, 7])
        4

        >>> find_greater_numbers([5, 4, 3, 2, 1])
        0

        >>> find_greater_numbers([])
        0
    """