def highest_frequency(nums):
    freq = {}
    
    for n in nums:
        freq[n] = freq.get(n, 0) + 1
    
    max_value = max(freq.values())
    
    for n in freq.keys():
        if freq[n] == max_value:
            return n



arr = [0, 1,11, 1, 1, 1, 34, 54, 3, 3, 3, 3 ,3]
result = highest_frequency(arr)
print(result)