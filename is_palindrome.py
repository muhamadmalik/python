# def isPalindrome(s ) :
#     l = 0
#     r = len(s) - 1
#     def isAlphaNum(c):
#         return ord('A') <=  ord(c) <= ord('Z') or ord('a') <= ord(c) <= ord('z') or ord('0') <= ord(c) <= ord('9')    
#     while l < r:
#         while l < r and  not isAlphaNum(s[l]):
#             l += 1
#         while l < r and not isAlphaNum(s[r]):
#             r -= 1
#             
#         if s[l].lower() != s[r].lower():
#             return False
#         
#         l += 1
#         r -= 1
#     return True    
# 
# 
# 



def isPalindrome( s) :
    def is_alphanum_char(char):
        return ('A' <= char <= 'Z') or ('a' <= char <= 'z') or ('0' <= char <= '9')
    l = 0
    r = len(s) - 1
    print(s)
    while l < r:
        while l < r and not is_alphanum_char(s[l]):
            print(s[l])
            l += 1
        while l < r and not is_alphanum_char(s[r]):
            r -= 1
        if s[l].lower() != s[r].lower():
            return False
        l += 1
        r -= 1
    return True

print(isPalindrome('A man, a plan, a canal: Panama'))
# print(isPalindrome('race a car'))