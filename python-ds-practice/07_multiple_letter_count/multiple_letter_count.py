def multiple_letter_count(phrase):
    """Return dict of {ltr: frequency} from phrase.

        >>> multiple_letter_count('yay')
        {'y': 2, 'a': 1}

        >>> multiple_letter_count('Yay')
        {'Y': 1, 'a': 1, 'y': 1}
    """
    # Initialize an empty dictionary to store the frequency count of each letter
    letter_count = {}
    
    # Iterate through each character in the phrase
    for letter in phrase:
        # Check if the letter is already in our dictionary
        if letter in letter_count:
            # If it is, increment its count by 1
            letter_count[letter] += 1
        else:
            # If not, add it to the dictionary with an initial count of 1
            letter_count[letter] = 1
    
    # Return the completed dictionary with all letter frequencies
    return letter_count
    
    # Time complexity: O(n) where n is the length of the phrase
    # Space complexity: O(k) where k is the number of unique characters in the phrase