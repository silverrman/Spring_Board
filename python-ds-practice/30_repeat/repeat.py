def repeat(phrase, num):
    """Return phrase, repeated num times.

    >>> repeat('hi', 2)
    'hihi'
    >>> repeat('hi', 0)
    ''
    """
    # Use string multiplication to repeat the phrase
    return phrase * num
    # Time complexity: O(n * m), where n is len(phrase) and m is num
    # Space complexity: O(n * m), for the new string
    """Return phrase, repeated num times.

        >>> repeat('*', 3)
        '***'

        >>> repeat('abc', 2)
        'abcabc'

        >>> repeat('abc', 0)
        ''

    Ignore illegal values of num and return None:

        >>> repeat('abc', -1) is None
        True

        >>> repeat('abc', 'nope') is None
        True
    """
