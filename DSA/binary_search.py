def binary_search(nums, target):
    nums.sort()
    left = 0
    right = len(nums) - 1 
    
    while left <= right:
        mid = (left + right) // 2
        
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1 
    return -1


result = binary_search([0, 2, 4, 3, 2, 9], 3)
print(result)