def is_odd_string(word):
    """Is the sum of the character-positions odd?

    Word is a simple word of uppercase/lowercase letters without punctuation.

    For each character, find it's "character position" ("a"=1, "b"=2, etc).
    Return True/False, depending on whether sum of those numbers is odd.

    For example, these sum to 1, which is odd:
    
        >>> is_odd_string('a')
        True

        >>> is_odd_string('A')
        True

    These sum to 4, which is not odd:
    
        >>> is_odd_string('aaaa')
        False

        >>> is_odd_string('AAaa')
        False

    Longer example:
    
        >>> is_odd_string('amazing')
        True
    """

    # Hint: you may find the ord() function useful here
    # Calculate the sum of character positions (a/A=1, b/B=2, ...)
    total = 0
    for char in word:
        # Normalize to lowercase to treat 'A' and 'a' the same
        total += ord(char.lower()) - ord('a') + 1
    # Return True if the sum is odd, False otherwise
    return total % 2 == 1
    # Time complexity: O(n), where n is the length of word
    # Space complexity: O(1), only needs a few variables