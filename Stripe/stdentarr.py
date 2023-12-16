def sortMatrixByKthExam(matrix, k):
    sorted_matrix = sorted(matrix, key=lambda x: x[k], reverse=True)
    return sorted_matrix

# Input matrix from the user
matrix_str = input("")

# Parse the input string to create the matrix
try:
    matrix = eval(matrix_str)
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise ValueError("Invalid input. Please enter a valid matrix.")
except (SyntaxError, ValueError) as e:
    print(f"Error: {e}")
    exit()

# Input k from the user
k = int(input(""))

result = sortMatrixByKthExam(matrix, k)
print(result)
