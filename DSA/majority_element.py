# def majority_element(nums):
#     hash = dict()
#     res = 0
#     max_num = 0
#     for i in nums: 
#         hash[i] = hash.get(i, 0) + 1
#         res = i if hash[i] > max_num else res
#         max_num = max(hash[i], max_num)
#     return res
# nums = [3,3, 4]
# print(majority_element(nums))
def majority_element(nums):
    count = 0
    res = 0
    for i in nums:
        if count == 0:
            res = i
        count = count + 1 if i == res else count - 1 
    return res
nums = [3,3, 4]
print(majority_element(nums))