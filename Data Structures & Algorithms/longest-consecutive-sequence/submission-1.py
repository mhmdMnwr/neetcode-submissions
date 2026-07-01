class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        history=set(nums)
        longestStreak=0
        currentStreak=0

        for num in nums:
            currentNum= num
            currentStreak=1

            while currentNum +1 in nums:
                currentStreak+=1
                currentNum+=1

            longestStreak= max(longestStreak , currentStreak)        
        return longestStreak