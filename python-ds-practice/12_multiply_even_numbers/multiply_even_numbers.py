def multiply_even_numbers(nums):
    """Multiply the even numbers.
    
        >>> multiply_even_numbers([2, 3, 4, 5, 6])
        48
        
        >>> multiply_even_numbers([3, 4, 5])
        4
        
    If there are no even numbers, return 1.
    
        >>> multiply_even_numbers([1, 3, 5])
        1
    """
    # Initialize product to 1 (neutral element for multiplication)
    product = 1
    found_even = False  # Flag to check if any even number is found
    
    # Iterate through each number in the list
    for num in nums:
        if num % 2 == 0:  # Check if the number is even
            product *= num  # Multiply the product by the even number
            found_even = True  # Mark that we found at least one even number
    
    # If no even numbers were found, product should remain 1
    return product if found_even else 1
    
    # Time complexity: O(n), where n is the length of nums
    # Space complexity: O(1), constant extra space