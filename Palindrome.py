class Solution:
    def isPalindrome(self, x: int) -> bool:
        num = x
        if x<0:
            return False
        else:
            revNum = 0
            while num != 0:
                revNum = revNum*10 + num % 10
                num = num//10
            if x == revNum:
                return True
            else:
                return False
        