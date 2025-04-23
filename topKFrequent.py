def topKFrequent(nums: list[int], k: int) -> list[int]:
    hash = dict()
    arr = []
    res = []
    for i in nums:
        hash[i] = 1 + hash.get(i, 0)
    # print(hash)
    
    for num, cnt in hash.items():
        arr.append((cnt, num))
    arr.sort()
    print(arr)
    
    while len(res) < k:
        
        res.append(arr.pop()[1])
    return res
arr = [1,2,3,2,3,2, 4, 4, 5,5, 5 , 5 ,5, 5, 5, 1,1,1,1,1,1,1,1,1,1,1 ]
    
k = 4
print(topKFrequent(arr, k))