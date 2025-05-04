def remove_every_other(lst):
    """Return a new list of other item.

        >>> lst = [1, 2, 3, 4, 5]

        >>> remove_every_other(lst)
        [1, 3, 5]

    This should return a list, not mutate the original:

        >>> lst
        [1, 2, 3, 4, 5]
    """
    # Use slicing to take every other element starting from index 0
    return lst[::2]
    # Time complexity: O(n), where n is the length of lst
    # Space complexity: O(n), for the new list
