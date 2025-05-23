def friend_date(a, b):
    """Given two friends, do they have any hobbies in common?

    - a: friend #1, a tuple of (name, age, list-of-hobbies)
    - b: same, for friend #2

    Returns True if they have any hobbies in common, False is not.

        >>> elmo = ('Elmo', 5, ['hugging', 'being nice'])
        >>> sauron = ('Sauron', 5000, ['killing hobbits', 'chess'])
        >>> gandalf = ('Gandalf', 10000, ['waving wands', 'chess'])

        >>> friend_date(elmo, sauron)
        False

        >>> friend_date(sauron, gandalf)
        True
    """
    # Extract the list of hobbies from each friend's tuple
    hobbies_a = set(a[2])
    hobbies_b = set(b[2])
    # Use set intersection to check for any common hobbies
    return len(hobbies_a & hobbies_b) > 0
    # Time complexity: O(n + m), where n and m are the number of hobbies for each friend
    # Space complexity: O(n + m), for storing the sets