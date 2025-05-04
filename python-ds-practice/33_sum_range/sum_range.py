def sum_range(nums, start=0, end=None):
    """Return sum of numbers from start...end.

    >>> sum_range([1, 2, 3, 4], 1, 3)
    5
    >>> sum_range([1, 2, 3, 4], 0, 2)
    3
    >>> sum_range([1, 2, 3, 4], 1)
    9
    >>> sum_range([1, 2, 3, 4])
    10
    """
    # If end is None, sum to the end of the list
    if end is None:
        end = len(nums)
    # Use slicing and sum
    return sum(nums[start:end])
    # Time complexity: O(n), where n is the slice length
    # Space complexity: O(n), for the slice
    """Return sum of numbers from start...end.

    - start: where to start (if not provided, start at list start)
    - end: where to stop (include this index) (if not provided, go through end)

        >>> nums = [1, 2, 3, 4]

        >>> sum_range(nums)
        10

        >>> sum_range(nums, 1)
        9

        >>> sum_range(nums, end=2)
        6

        >>> sum_range(nums, 1, 3)
        9

    If end is after end of list, just go to end of list:

        >>> sum_range(nums, 1, 99)
        9
    """
