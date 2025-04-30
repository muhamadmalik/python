def maxArea(heights):
    res = 0
    l = 0
    r = len(heights) - 1
    i = len(heights) - 1
    
    while l < r:
        rectangle_area = min(heights[l], heights[r]) * i
        res = max(res, rectangle_area)
        i -= 1
        if heights[l] < heights[r]:
            l += 1
        else:
            r -= 1
    return res


height = [2,2,2]
result = maxArea(height)
print(result)