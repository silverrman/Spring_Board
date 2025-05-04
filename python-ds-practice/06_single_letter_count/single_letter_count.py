def single_letter_count(word, letter, case_sensitive=False):
    """How many times does letter appear in word?

    If case_sensitive is False (default), count is case-insensitive.
    If case_sensitive is True, count is case-sensitive.

        >>> single_letter_count('Hello World', 'h')
        1
        >>> single_letter_count('Hello World', 'z')
        0
        >>> single_letter_count("Hello World", 'l')
        3
        >>> single_letter_count("Hello World", 'L')
        3
        >>> single_letter_count("Hello World", 'l', case_sensitive=True)
        3
        >>> single_letter_count("Hello World", 'L', case_sensitive=True)
        0
    """
    # This function counts how many times a specific letter appears in a word
    # It has an optional parameter to control case sensitivity
    
    # Check if case sensitivity is required
    if case_sensitive:
        # Use the string's count() method to count occurrences of the exact letter
        # This will be case-sensitive (e.g., 'a' != 'A')
        return word.count(letter)
    else:
        # For case-insensitive counting, convert both the word and letter to lowercase
        # Then count occurrences of the lowercase letter in the lowercase word
        return word.lower().count(letter.lower())
    
    # Time complexity: O(n) where n is the length of the word
    # Space complexity: O(n) if case_sensitive=False (for creating lowercase string)