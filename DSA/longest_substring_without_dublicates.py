class Solution:
    def longest_substring(self, s):
        char_set = set()
        res = 0
        l = 0
        
        for r in range(len(s)):
            while s[r] in char_set:
                char_set.remove(s[l])
                l += 1
            char_set.add(s[r])
            res = max(res, r - l + 1)
        return res

s = 'abcabcbabklisl'

statement = Solution()
result = statement.longest_substring(s)
print(result)