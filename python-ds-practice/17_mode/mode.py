def mode(nums):
    """Return most-common number in list.

    For this function, there will always be a single-most-common value;
    you do not need to worry about handling cases where more than one item
    occurs the same number of times.

        >>> mode([1, 2, 1])
        1

        >>> mode([2, 2, 3, 3, 2])
        2
    """
    # Create a dictionary to count occurrences of each number
    counts = {}
    for num in nums:
        counts[num] = counts.get(num, 0) + 1
    
    # Find the number with the highest count
    # max returns the key with the maximum value in the dictionary
    return max(counts, key=counts.get)
    
    # Time complexity: O(n), where n is the length of nums
    # Space complexity: O(k), where k is the number of unique elements
