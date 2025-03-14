"""
217. Contains Duplicate
Easy
Topics
Companies
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

 

Example 1:

Input: nums = [1,2,3,1]

Output: true

Explanation:

The element 1 occurs at the indices 0 and 3.

Example 2:

Input: nums = [1,2,3,4]

Output: false

Explanation:

All elements are distinct.

Example 3:

Input: nums = [1,1,1,3,3,4,3,2,4,2]

Output: true

 

Constraints:

1 <= nums.length <= 105
-109 <= nums[i] <= 109
"""
# def containDuplicate(nums):
#     new_array = []
#     for num in range(len(nums)):
#         print(num)
#         if(new_array.__contains__(nums[num])):
#             print(new_array)
#             return True
#         else:
#             new_array.append(nums[num])
#             print(new_array)
#     return False
# 
# nums = [1,3,2,4,2]
# print(containDuplicate(nums))

# 
# def containDuplicate(nums):
#     hash_set = set()
#     for n in range(len(nums)):
#         if nums[n] in hash_set:
#             return True
#         hash_set.add(nums[n])
#     return False
# 
# nums = [1,3,2,4]
# print(containDuplicate(nums))

def containDuplicate(nums):
    hash_set = set(nums)
    if len(hash_set) < len(nums):
        return True
    return False

nums = [1,3,2,4,4]
print(containDuplicate(nums))
        