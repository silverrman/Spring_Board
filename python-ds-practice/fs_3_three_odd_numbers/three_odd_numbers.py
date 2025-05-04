def three_odd_numbers(nums):
    """Is the sum of any 3 sequential numbers odd?"

        >>> three_odd_numbers([1, 2, 3, 4, 5])
        True

        >>> three_odd_numbers([0, -2, 4, 1, 9, 12, 4, 1, 0])
        True

        >>> three_odd_numbers([5, 2, 1])
        False

        >>> three_odd_numbers([1, 2, 3, 3, 2])
        False
    """
    # Check every window of 3 sequential numbers
    for i in range(len(nums) - 2):
        window_sum = nums[i] + nums[i+1] + nums[i+2]
        if window_sum % 2 == 1:
            return True
    return False
    # Time complexity: O(n), where n is the length of nums
    # Space complexity: O(1)
