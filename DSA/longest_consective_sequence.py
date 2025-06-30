def longestConsecutive(nums):
    
    seen = set()
    longest = 0
    for i in range(len(nums)):
        number = nums[i]
        seen.add(number)
        
    print(seen)
    for i in range(len(nums)):
        if (nums[i] - 1) not in seen:
            length = 1
            while (nums[i] + length) in seen:
                length += 1
                longest = max(longest, length)
    return longest

nums = [100, 4, 200, 1, 3, 2]
result = longestConsecutive(nums)
print(result) 