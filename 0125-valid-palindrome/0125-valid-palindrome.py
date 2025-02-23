class Solution:
    def isPalindrome(self, s: str) -> bool:
        n=len(s)
        left,right=0,n-1

        while(left<right):
            if not s[left].isalnum():
                left+=1
            if not s[right].isalnum():
                right-=1
            if s[left].isalnum() and s[right].isalnum():
                if s[left].lower()==s[right].lower():
                    left+=1
                    right-=1
                else:
                    return False
        return True


#         s=s.lower()
#         left,right=0,len(s)-1

#         #[',lakl]

#         while(left<right):
#             if(not isAlphanumeric(s[left])):
#                 left+=1
#             elif(not isAlphanumeric(s[right])):
#                 right-=1
#             if(isAlphanumeric(s[left]) and isAlphanumeric(s[right])):
#                 if(s[left]==s[right]):
#                     left+=1
#                     right-=1
#                 else:
#                     return False
#         return True


# def isAlphanumeric(ch):
#     return (ord('A')<=ord(ch)<=ord('Z') or
#             ord('a')<=ord(ch)<=ord('z') or
#             ord('0')<=ord(ch)<=ord('9'))