# def twoSum(nums, target):
#     hash_map = dict()
#     for n in range(len(nums)):
#         difference = target - nums[n]
#         if difference in hash_map:
#             return [hash_map.get(difference), n]
#         else:
#             hash_map[nums[n]] = n
#     return []
# print(twoSum([2, 7, 11, 15], 9))
# 

def twoSum(nums, target):
    map = dict()
    
    for i in range(len(nums)):
        diff = target - nums[i]
        if diff in map:
            return [map[diff] , i]
        else:
            map[nums[i]] = i
    return []
        
        
print(twoSum([2, 7, 11, 15], 26))