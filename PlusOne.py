class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        strNum = ""
        for i in digits:
            strNum = strNum + str(i)
        n = int(strNum) + 1
        strNum = str(n)
        out = []
        for i in strNum:
            out.append(int(i))
        return out