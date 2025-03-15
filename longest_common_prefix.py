def longestCommonPrefix(strs: list[str]) -> str:
    ans = ''
    for i in range(len(strs[0])):
        for str in strs:
            if i == len(str) or str[i] != strs[0][i]:
                return ans
        ans = ans + str[i]
    return ans


strs = ["flower"]
print(longestCommonPrefix(strs))