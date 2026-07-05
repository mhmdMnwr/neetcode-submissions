class Solution:
    def trap(self, height: List[int]) -> int:
        if not height: return 0
        res=0
        n=len(height)
        for i in range(n):
            right=left=height[i]

            for j in range(i+1,n):
                right=max(right,height[j])
            for j in range(i):
                left=max(left,height[j])
            res+=min(left,right)-height[i]
        return res