
def isAnagram(s, t):
    countS = dict()
    countT = dict()
    if len(s) != len(t):
        return False
        
    for n in range(len(s)):
        countS[s[n]] = countS.get(s[n], 0) + 1 
        countT[t[n]] = countT.get(t[n], 0) + 1
    
    for n in range(len(s)):
        if countS.get(s[n], 0) != countT.get(s[n], 0):
            return False
    return True
s = "jar"
t = "jra"
print(isAnagram(s, t))
