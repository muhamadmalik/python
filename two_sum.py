def twoSum(nums, target):
    hash_map = dict()
    for n in range(len(nums)):
        difference = target - nums[n]
        if difference in hash_map:
           return  [ hash_map[difference], n]
        else:
            print(f"I'm storing {nums[n]} as key and {n} as a answer")
            hash_map[nums[n]] = n
    return []
print(twoSum([2, 7, 11, 15], 9))



