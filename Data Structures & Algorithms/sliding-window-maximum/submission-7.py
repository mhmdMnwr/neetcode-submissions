class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums: return []
        if len(nums)<k :
            mm=nums[0]
            for num in nums:
                mm=max(mm,num)
            return mm
        current_nums=[]
        l=0
        r=k-1
        res=[]

        while r<len(nums):
            mx=nums[l]
            for i in range(l,r+1):
                mx=max(mx,nums[i])
            res.append(mx)
            r+=1
            l+=1

        return res

        