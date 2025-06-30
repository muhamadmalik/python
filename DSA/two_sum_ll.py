def twoSum(nums, target):
    l = 0
    r = len(nums) - 1 
    while l < r:
        sum = nums[l] + nums[r] 
        if sum > target:
            r -= 1
        elif sum < target:
            l += 1
        else:
            return [l+1, r+1]
    return []

numbers = [1,2, 5]
target = 3

print(twoSum(numbers, target))