def min_max_key_in_dictionary(d):
    """Return tuple (min-key, max-key) in dictionary.

    >>> min_max_key_in_dictionary({"apple": 2, "pear": 1, "orange": 3})
    ('pear', 'orange')
    >>> min_max_key_in_dictionary({1: 'a', 2: 'b', 3: 'c'})
    (1, 3)
    """
    # Use min and max functions on the dictionary keys
    keys = d.keys()
    return (min(keys), max(keys))
    # Time complexity: O(n), where n is the number of keys
    # Space complexity: O(1)

def min_max_keys(d):
    """Return tuple (min-keys, max-keys) in d.

        >>> min_max_keys({2: 'a', 7: 'b', 1: 'c', 10: 'd', 4: 'e'})
        (1, 10)

    Works with any kind of key that can be compared, like strings:

        >>> min_max_keys({"apple": "red", "cherry": "red", "berry": "blue"})
        ('apple', 'cherry')
    """