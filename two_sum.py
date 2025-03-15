def twoSum(nums, target):
    hash_map = dict()
    for n in range(len(nums)):
        difference = target - nums[n]
        if difference in hash_map:
            return [hash_map.get(difference), n]
        else:
            hash_map[nums[n]] = n
    return []
print(twoSum([2, 7, 11, 15], 9))



