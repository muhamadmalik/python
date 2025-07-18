         [    
matrix = [1, 2],
         [3, 4]
         ]
left = 0
right = len(matrix[0])

top = 0
bottom = len(matrix)
res = []

while left < right and top < bottom:
    for i in range(left, right):
        res.append(matrix[top][i])
    top += 1

    for i in range(top, bottom)
        res.append(matrix[i][])
    
