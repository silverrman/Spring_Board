def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """
    # Convert to_swap to lowercase for case-insensitive comparison
    to_swap_lower = to_swap.lower()
    # Initialize an empty result string
    result = ""
    
    # Iterate through each character in the phrase
    for char in phrase:
        # Check if the lowercase version of the current character matches to_swap_lower
        if char.lower() == to_swap_lower:
            # If it matches, flip its case using the swapcase() method
            result += char.swapcase()
        else:
            # If it doesn't match, keep it as is
            result += char
    
    return result
    
    # Time complexity: O(n) where n is the length of the phrase
    # Space complexity: O(n) for storing the result string
