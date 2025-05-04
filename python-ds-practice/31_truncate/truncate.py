def truncate(phrase, n):
    """Return truncated string at n characters, with '...' if longer.

    >>> truncate('Hello World', 6)
    'Hel...'
    >>> truncate('Problem solving is the best!', 10)
    'Problem...'
    >>> truncate('Yo', 100)
    'Yo'
    """
    # If n is less than 3, return 'Truncation must be at least 3 characters.'
    if n < 3:
        return 'Truncation must be at least 3 characters.'
    # If the phrase is longer than n, return the first n-3 chars + '...'
    if len(phrase) > n:
        return phrase[:n-3] + '...'
    # Otherwise, return the phrase as is
    return phrase
    # Time complexity: O(n), where n is the truncation length
    # Space complexity: O(n), for the new string
    """Return truncated-at-n-chars version of  phrase.
    
    If the phrase is longer than, or the same size as, n make sure it ends with '...' and is no
    longer than n.
    
        >>> truncate("Hello World", 6)
        'Hel...'
        
        >>> truncate("Problem solving is the best!", 10)
        'Problem...'
        
        >>> truncate("Yo", 100)
        'Yo'
        
    The smallest legal value of n is 3; if less, return a message:
    
        >>> truncate('Cool', 1)
        'Truncation must be at least 3 characters.'

        >>> truncate("Woah", 4)
        'W...'

        >>> truncate("Woah", 3)
        '...'
    """