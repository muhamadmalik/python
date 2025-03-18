def removeElement( nums: list[int], val: int) -> int:
    k = 0
    for i in range(len(nums)):
        if nums[i] != val:
            nums[k] = nums[i]
            k += 1
    return k
        
nums = [3,2,2,3, 34, 434, 45]
print(removeElement(nums, 2))