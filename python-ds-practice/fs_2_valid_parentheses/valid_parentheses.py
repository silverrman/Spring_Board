def valid_parentheses(parens):
    """Are the parentheses validly balanced?

        >>> valid_parentheses("()")
        True

        >>> valid_parentheses("()()")
        True

        >>> valid_parentheses("(()())")
        True

        >>> valid_parentheses(")()")
        False

        >>> valid_parentheses("())")
        False

        >>> valid_parentheses("((())")
        False

        >>> valid_parentheses(")()(")
        False
    """
    # Use a counter to track open parentheses
    count = 0
    for char in parens:
        if char == '(': count += 1
        elif char == ')':
            count -= 1
            if count < 0:
                return False
    return count == 0
    # Time complexity: O(n), where n is the length of parens
    # Space complexity: O(1)