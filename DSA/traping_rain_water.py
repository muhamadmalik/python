class Solution:
    def trap(self, height: list[int]) -> int:
        if not height:
            return 0
        res  = 0
        l = 0
        r = len(height) - 1
        leftMax = height[l]
        rightMax = height[r]
        
        while l < r:
            if leftMax < rightMax:
                l += 1
                leftMax = max(leftMax, height[l])
                res +=  leftMax - height[l]
            else:
                r -= 1
                rightMax = max(rightMax, height[r])
                res += rightMax - height[r]
        return res
    
height = [0,2,0,3,1,0,1,3,2,1]

statement = Solution()
result = statement.trap(height)
print(result)