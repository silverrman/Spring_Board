def reverse_string(phrase):
    """Reverse string,

        >>> reverse_string('awesome')
        'emosewa'

        >>> reverse_string('sauce')
        'ecuas'
    """
    # Reverse the string using slice notation with a step of -1
    # In Python, phrase[::-1] creates a slice of the entire string (phrase[:]) with a step of -1
    # The -1 step means to iterate through the string in reverse order
    # This is a pythonic way to reverse a sequence (string, list, etc.)
    return phrase[::-1]
    
    # Time complexity: O(n) where n is the length of the string
    # Space complexity: O(n) for creating the new reversed string
