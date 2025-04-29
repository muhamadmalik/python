def sortColors(nums):
    l = 0
    r = len(nums) - 1
    i = 0
    def swap(i, j):
        temp = nums[i]
        nums[i] = nums[j]
        nums[j] = temp
    
    while i <= r:
        if nums[i] == 0:
            swap(l, i)
            l += 1
        elif nums[i] == 2:
            swap(i,r)
            r -= 1
            i -= 1
        i += 1
    return nums

print(sortColors([2, 0, 2, 1, 1, 0]))