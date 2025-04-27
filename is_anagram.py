
# def isAnagram(s, t):
    # countS = dict()
    # countT = dict()
    # if len(s) != len(t):
    #     return False
    #     
    # for n in range(len(s)):
    #     countS[s[n]] = countS.get(s[n], 0) + 1 
    #     countT[t[n]] = countT.get(t[n], 0) + 1
    # 
    # for n in range(len(s)):
    #     if countS.get(s[n], 0) != countT.get(s[n], 0):
    #         return False
    # return True
    
def isAnagram(s, t):        
    countS = dict()
    countT = dict()
    
    if len(s) != len(t):
        return False
    for i in range(len(s)):
        countS[s[i]] = countS.get(s[i], 0) + 1
        countT[t[i]] = countT.get(t[i], 0) + 1

    
    if countS[s[i]] != countT[t[i]]:
            return False
    return True
        

s = "jar"
t = "ja"
print(isAnagram(s, t))