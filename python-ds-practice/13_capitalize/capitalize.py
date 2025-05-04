def capitalize(phrase):
    """Capitalize first letter of first word of phrase.

        >>> capitalize('python')
        'Python'

        >>> capitalize('only first word')
        'Only first word'
    """
    # Use the built-in string method capitalize(), which capitalizes only the first character
    # and lowercases the rest of the string. However, to match the docstring, we want only
    # the first character capitalized, and the rest of the phrase unchanged.
    if not phrase:
        return ''  # Handle empty string
    # Capitalize the first character, keep the rest of the phrase unchanged
    return phrase[0].upper() + phrase[1:]
    
    # Time complexity: O(n), where n is the length of the phrase
    # Space complexity: O(n), for creating the new string