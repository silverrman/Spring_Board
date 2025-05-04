def same_frequency(num1, num2):
    """Do these nums have same frequencies of digits?

    >>> same_frequency(551122, 221515)
    True
    >>> same_frequency(321142, 3212215)
    False
    >>> same_frequency(1212, 2211)
    True
    """
    # Convert numbers to strings and count digit frequencies
    from collections import Counter
    return Counter(str(num1)) == Counter(str(num2))
    # Time complexity: O(n + m), where n and m are the number of digits
    # Space complexity: O(n + m), for the counters
    """Do these nums have same frequencies of digits?
    
        >>> same_frequency(551122, 221515)
        True
        
        >>> same_frequency(321142, 3212215)
        False
        
        >>> same_frequency(1212, 2211)
        True
    """