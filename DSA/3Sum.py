def threeSum(nums):
    res = []
    nums.sort()
    
    for i in range(len(nums)):
        l = i + 1
        r = len(nums) - 1
        
        if nums[i] > 0:
            break
        
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        
        while l < r:
            threeSum = nums[i] + nums[l] + nums[r]
            if threeSum > 0:
                r -= 1
            if threeSum < 0:
                l += 1
            else:
                res.append([nums[i] , nums[l] , nums[r]])
                l += 1
                r -= 1
                while nums[l] == nums[l - 1] and l < r:
                    l += 1
    return res
nums = [-1, 0, 1, 2, -1, -4]

result = threeSum(nums)
print(result)