def find_the_duplicate(nums):
    """Return first duplicate value found in nums.

    >>> find_the_duplicate([1, 2, 1, 4, 3, 12])
    1
    >>> find_the_duplicate([6, 1, 9, 5, 3, 7, 9, 10, 2, 1])
    9
    >>> find_the_duplicate([2, 1, 3, 4])
    None
    """
    seen = set()
    for num in nums:
        if num in seen:
            return num
        seen.add(num)
    return None
    # Time complexity: O(n), where n is the length of nums
    # Space complexity: O(n), for the set
    """Find duplicate number in nums.

    Given a list of nums with, at most, one duplicate, return the duplicate.
    If there is no duplicate, return None

        >>> find_the_duplicate([1, 2, 1, 4, 3, 12])
        1

        >>> find_the_duplicate([6, 1, 9, 5, 3, 4, 9])
        9

        >>> find_the_duplicate([2, 1, 3, 4]) is None
        True
    """
