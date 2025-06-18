
def sortArray(nums):
    def merge(arr, L, M, R):
        left = arr[L:M+1]
        right = arr[M + 1: R + 1]
        
        j = 0
        k = 0
        i = L
        
        while j < len(left) and k < len(right):
            if left[j] <= right[k]:
                arr[i] = left[j]
                j += 1
            else:
                arr[i] = right[k]
                k += 1
            i += 1
        
        while j < len(left):
            arr[i] = left[j]
            j += 1
            i += 1
        while k < len(right):
            arr[i] = right[k]
            k += 1
            i += 1
    
    
    def mergeSort(arr, l, r):
        print(arr)
        if l == r:
            return 
        m = (l + r) // 2
        mergeSort(arr, l, m)
        mergeSort(arr, m + 1, r)
        merge(arr, l, m, r)
        return 
    
    mergeSort(nums, 0, len(nums))
    return nums
        


nums = [5, 4, 3, 2, 1, 1, 0]
# print(nums[1: 3])
print(sortArray(nums))