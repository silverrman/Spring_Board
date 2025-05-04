def titleize(phrase):
    """Return phrase in title case (each word capitalized).

    >>> titleize('this is awesome')
    'This Is Awesome'
    """
    # Use the built-in title() method to capitalize each word
    return phrase.title()
    # Time complexity: O(n), where n is the length of phrase
    # Space complexity: O(n), for the new string
    """Return phrase in title case (each word capitalized).

        >>> titleize('this is awesome')
        'This Is Awesome'

        >>> titleize('oNLy cAPITALIZe fIRSt')
        'Only Capitalize First'
    """
