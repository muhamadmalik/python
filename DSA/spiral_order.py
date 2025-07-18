def spiralOrder(matrix: list[list[int]]) -> list[int]:
    res = []
    left, right = 0, len(matrix[0])
    top, bottom = 0, len(matrix)
    matrix_length = len(matrix) * len(matrix[0])
    
    while left < right and top < bottom:
        for i in range(left, right):
            res.append(matrix[top][i])
        top += 1
        for i in range(top, bottom):
            res.append(matrix[i][right - 1])
        right -= 1
        if len(res) == matrix_length:
            break
        for i in range(right - 1, left - 1, -1):
            res.append(matrix[bottom - 1][i])
        bottom -= 1
        for i in range(bottom - 1, top - 1, -1):
            res.append(matrix[i][left])
        left += 1
    return res



matrix=[[1,2,3,4],[5,6,7,8],[9,10,11,12]]

output = [1, 2, 3,
          6, 9, 8,
          7, 4, 5]
result = spiralOrder(matrix)
print(result)

