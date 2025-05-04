def find_factors(num):
    """Find factors of num, in increasing order.

    >>> find_factors(10)
    [1, 2, 5, 10]
    >>> find_factors(11)
    [1, 11]
    >>> find_factors(111)
    [1, 3, 37, 111]
    >>> find_factors(321421)
    [1, 13, 24647, 321421]
    """
    # Use list comprehension to collect all divisors of num
    return [i for i in range(1, num + 1) if num % i == 0]
    # Time complexity: O(n), where n is the value of num
    # Space complexity: O(k), where k is the number of factors
    """Find factors of num, in increasing order.

    >>> find_factors(10)
    [1, 2, 5, 10]

    >>> find_factors(11)
    [1, 11]

    >>> find_factors(111)
    [1, 3, 37, 111]

    >>> find_factors(321421)
    [1, 293, 1097, 321421]
    """
