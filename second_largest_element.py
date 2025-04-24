def findKthLargest(nums, k):
    k = len(nums) - k
    def quickSelect(l, r):
        pivot = nums[r]
        p = l
        for i in range(l, r):
            if nums[i] <=  pivot:
                temp = nums[p]
                nums[p] = nums[i]
                nums[i] = temp
                p += 1
        temp2 = nums[p]
        nums[p] = nums[r]
        nums[r] = temp2
        if p < k:
           return quickSelect(p + 1, r)
        elif p > k:
            return quickSelect(l, p - 1)
        else :
            return nums[p]
    return quickSelect(0, len(nums) - 1)
   

print(findKthLargest([3,2,1,5,6,4], 2))