def reverse_vowels(s):
    """
    # Identify vowels
    vowels = set('aeiouAEIOU')
    s_list = list(s)
    # Collect indices and vowels
    vowel_indices = [i for i, char in enumerate(s_list) if char in vowels]
    vowel_chars = [s_list[i] for i in vowel_indices][::-1]
    # Replace original vowels with reversed
    for idx, vi in enumerate(vowel_indices):
        s_list[vi] = vowel_chars[idx]
    return ''.join(s_list)
    # Time complexity: O(n), where n is the length of s
    # Space complexity: O(n), for the new list
    """
    # Identify vowels
    vowels = set('aeiouAEIOU')
    s_list = list(s)
    # Collect indices and vowels
    vowel_indices = [i for i, char in enumerate(s_list) if char in vowels]
    vowel_chars = [s_list[i] for i in vowel_indices][::-1]
    # Replace original vowels with reversed
    for idx, vi in enumerate(vowel_indices):
        s_list[vi] = vowel_chars[idx]
    return ''.join(s_list)
    # Time complexity: O(n), where n is the length of s
    # Space complexity: O(n), for the new list

    """
    Reverse vowels in a string.

    Characters which re not vowels do not change position in string, but all
    vowels (y is not a vowel), should reverse their order.

    >>> reverse_vowels("Hello!")
    'Holle!'

    >>> reverse_vowels("Tomatoes")
    'Temotaos'

    >>> reverse_vowels("Reverse Vowels In A String")
    'RivArsI Vewols en e Streng'

    reverse_vowels("aeiou")
    'uoiea'

    reverse_vowels("why try, shy fly?")
    'why try, shy fly?''
    """