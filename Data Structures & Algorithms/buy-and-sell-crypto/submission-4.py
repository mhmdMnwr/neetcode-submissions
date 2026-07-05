class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res=0
        n=len(prices)
        l=0
        r=1
        while r < n:
            if prices[r] > prices[l]:
                res=max(res, prices[r] - prices[l])
                
            else:
                l=r
            r+=1
        return res        