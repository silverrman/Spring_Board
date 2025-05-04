def is_palindrome(phrase):
    """Is phrase a palindrome?

    Return True/False if phrase is a palindrome (same read backwards and
    forwards).

        >>> is_palindrome('tacocat')
        True

        >>> is_palindrome('noon')
        True

        >>> is_palindrome('robert')
        False

    Should ignore capitalization/spaces when deciding:

        >>> is_palindrome('taco cat')
        True

        >>> is_palindrome('Noon')
        True
    """
    # A palindrome reads the same forwards and backwards (ignoring case and spaces)
    
    # Convert the phrase to lowercase to make the comparison case-insensitive
    # Remove all spaces to ignore them in the comparison
    # We use the replace() method to remove spaces
    normalized = phrase.lower().replace(" ", "")
    
    # Compare the normalized string with its reverse
    # If they are the same, the phrase is a palindrome
    # We use slicing [::-1] to reverse the string efficiently
    return normalized == normalized[::-1]
    
    # Time complexity: O(n) where n is the length of the phrase
    # Space complexity: O(n) for storing the normalized string
