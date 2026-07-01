class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen=set(nums)
        if not seen: return 0
        res=0
        streak=1
        for num in nums:
            streak=1
            currentNum = num
            while currentNum +1 in nums:
                streak+=1
                currentNum+=1
            res = max(res,streak)
        return res