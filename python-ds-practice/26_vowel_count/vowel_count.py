def vowel_count(phrase):
    """Return frequency map of vowels, case-insensitive.

    >>> vowel_count('awesome')
    {'a': 1, 'e': 2, 'o': 1}
    >>> vowel_count('Awesome')
    {'a': 1, 'e': 2, 'o': 1}
    >>> vowel_count('Yay!')
    {'a': 1}
    """
    # Define a set of vowels
    vowels = set('aeiou')
    count = {}
    for char in phrase.lower():
        if char in vowels:
            count[char] = count.get(char, 0) + 1
    return count
    # Time complexity: O(n), where n is the length of phrase
    # Space complexity: O(1), since the number of vowels is fixed
    """Return frequency map of vowels, case-insensitive.

        >>> vowel_count('rithm school')
        {'i': 1, 'o': 2}
        
        >>> vowel_count('HOW ARE YOU? i am great!') 
        {'o': 2, 'a': 3, 'e': 2, 'u': 1, 'i': 1}
    """