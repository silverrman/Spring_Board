def sum_up_diagonals(matrix):
    """Return sum of both diagonals in a square matrix.

    >>> sum_up_diagonals([[1, 2], [3, 4]])
    10
    >>> sum_up_diagonals([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    30
    """
    n = len(matrix)
    total = 0
    for i in range(n):
        total += matrix[i][i]            # main diagonal
        total += matrix[i][n - 1 - i]    # secondary diagonal
    # If n is odd, subtract the center element (counted twice)
    if n % 2 == 1:
        total -= matrix[n // 2][n // 2]
    return total
    # Time complexity: O(n), where n is the size of the matrix
    # Space complexity: O(1)
    """Given a matrix [square list of lists], return sum of diagonals.

    Sum of TL-to-BR diagonal along with BL-to-TR diagonal:

        >>> m1 = [
        ...     [1,   2],
        ...     [30, 40],
        ... ]
        >>> sum_up_diagonals(m1)
        73

        >>> m2 = [
        ...    [1, 2, 3],
        ...    [4, 5, 6],
        ...    [7, 8, 9],
        ... ]
        >>> sum_up_diagonals(m2)
        30
    """