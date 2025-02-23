class Solution:
    def hasSameDigits(self, s: str) -> bool:
        res_len=len(s)
        while(res_len>2):
            res=''
            for i in range(1,len(s)):
                res=res+ str((int(s[i])+int(s[i-1]))%10)
            res_len=len(res)
            s=res

        return True if s[0]==s[1] else False
    