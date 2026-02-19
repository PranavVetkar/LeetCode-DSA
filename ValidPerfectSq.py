class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num == 1 or num == 4:
            return True
        else:
            for i in range(2, int(num ** 0.5)+1):
                if i**2 == num:
                    return True
            return False
