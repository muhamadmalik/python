from collections import defaultdict

# def groupAnagrams(strs: list[str]) -> list[list[str]]:
#     res = defaultdict(list)
#     for s in strs:
#         sortedS = "".join(sorted(s))
#         res[sortedS].append(s)
#         
#     return list(res.values())




def groupAnagrams(strs: list[str]) -> list[list[str]]: 
        res = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            res[tuple(count)].append(s)
        return list(res.values())
    
strs = ["act","pots","tops","cat","stop","hat", "het"]

print(groupAnagrams(strs))