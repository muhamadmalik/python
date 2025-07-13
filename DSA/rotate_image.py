from typing import List

# class Solution:
#     def rotate(self, matrix: List[List[int]]) -> None:
#         
#         left = 0
#         right = len(matrix) - 1
#         
#         while left < right:
#             top = left 
#             bottom = right 
#             
#             for i in range(right - left):
#                 top_left = matrix[top][left + i]
#                 
#                 matrix[top][left + i]  = matrix[bottom - i][left]
#                 matrix[bottom - i][left] = matrix[bottom][right - i]
#                 matrix[bottom][right - i] = matrix[top + i][right]
#                 matrix[top + i][right] = top_left
#             left += 1
#             right -= i
        
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
                
                matrix[top][left + i]  = matrix[bottom - i][left]
                matrix[bottom - i][left] = matrix[bottom][right - i]
                matrix[bottom][right - i] = matrix[top + i][right]
                matrix[top + i][right] = top_left
            left += 1
            right -= i
        

# Example of how to use it:
sol = Solution()
my_matrix = [[1,2,3],[4,5,6],[7,8,9]]
sol.rotate(my_matrix)
print(my_matrix)

my_matrix_2 = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
sol.rotate(my_matrix_2)
print(my_matrix_2)