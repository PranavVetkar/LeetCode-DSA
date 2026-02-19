class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        flag = 0
        for i in range(0,len(haystack)-len(needle)+1):
            if haystack[i:i+len(needle)] == needle:
                flag = 1
                return i
        if flag == 0:
            return -1
            
