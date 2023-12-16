def generate_pascals_triangle(numRows):
    if numRows == 0:
        return []

    triangle = [[1]]

    for _ in range(1, numRows):
        prev_row = triangle[-1]
        new_row = [1] + [prev_row[i - 1] + prev_row[i] for i in range(1, len(prev_row))] + [1]

        triangle.append(new_row)

    return triangle

numRows = int(input(""))
result = generate_pascals_triangle(numRows)
print(result)