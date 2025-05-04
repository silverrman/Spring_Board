def number_compare(a, b):
    """Report on whether a>b, b>a, or b==a
    
        >>> number_compare(1, 1)
        'Numbers are equal'
        
        >>> number_compare(-1, 1)
        'Second is greater'
        
        >>> number_compare(1, -2)
        'First is greater'
    """
    # Compare two numbers and return a string describing their relationship
    
    # Check if the first number is greater than the second
    if a > b:
        return "First is greater"
    # Check if the second number is greater than the first
    elif b > a:
        return "Second is greater"
    # If neither condition is met, the numbers must be equal
    else:
        return "Numbers are equal"
    
    # Time complexity: O(1) - simple comparison operations
    # Space complexity: O(1) - constant space used regardless of input size