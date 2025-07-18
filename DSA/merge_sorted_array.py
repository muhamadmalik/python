def merge(nums1: list[int], m: int, nums2: list[int], n: int) -> None:
    
    last = len(nums1) - 1
    
    
    while m > 0 and n > 0:
        if nums1[m - 1] > nums2[n - 1]:
            nums1[last] = nums1[m - 1]
            m -= 1
        else:
            nums1[last]  = nums1[n - 1] 
            n -= 1
        last -= 1
    while n > 0:
        nums1[last] = nums2[n - 1]
        n -= 1
        last -= 1
    
    return nums1
        
nums1 = [10,20,20,40,0,0]
m = 4 # the number of valid number in nums1
nums2 = [1,2]
n = 2 # the number of total numbers in nums2 

result = merge(nums1, m, nums2, n)
print(result)
    
        
        

     
    
