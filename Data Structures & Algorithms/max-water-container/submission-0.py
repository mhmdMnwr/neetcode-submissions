class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left=0
        right=0
        maximum=0
        for i in range(len(heights)):
            for j in range(i+1,len(heights)):
                maximum=max(maximum,(j-i)*min(heights[i],heights[j]))
        return maximum