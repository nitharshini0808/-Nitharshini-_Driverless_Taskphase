def matrix_multiply(A, B):
    
    if not A or not A[0] or not B or not B[0]:
        print("Error: one of the matrices is empty.")
        return None

    rows_A, cols_A = len(A), len(A[0])
    rows_B, cols_B = len(B), len(B[0])

    
    if any(len(row) != cols_A for row in A):
        print("Error: matrix A has rows of inconsistent length.")
        return None

    
    if any(len(row) != cols_B for row in B):
        print("Error: matrix B has rows of inconsistent length.")
        return None

    
    if cols_A != rows_B:
        print(f"Error: cannot multiply a {rows_A}x{cols_A} matrix "
              f"by a {rows_B}x{cols_B} matrix (inner dimensions must match).")
        return None

    result = [[0] * cols_B for _ in range(rows_A)]
    for i in range(rows_A):
        for j in range(cols_B):
            total = 0
            for k in range(cols_A):
                total += A[i][k] * B[k][j]
            result[i][j] = total

    return result  

A = [[1, 2],
     [3, 6]]

B = [[5, 6],
     [7, 8]]

result = matrix_multiply(A, B)

print(result)

