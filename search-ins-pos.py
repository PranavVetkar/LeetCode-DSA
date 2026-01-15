class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        flag = 1
        for i in range(0,len(nums)):
            if target == nums[i]:
                return i
                flag = 0
                break
        if flag == 1:
            nums.append(target)
            nums.sort()
            for i in range(0,len(nums)):
                if target == nums[i]:
                    print(i)
                    return i
                    break
