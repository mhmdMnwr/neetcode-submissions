class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left=0
        right=len(heights)-1
        maximum=0
        while left<right:
            minHeigth=min(heights[left],heights[right])
            maximum=max(maximum,(right-left)* minHeigth)
            if heights[left]== minHeigth:
                while left<right and minHeigth >= heights[left]:
                    left+=1
            else: 
                while left<right and minHeigth >= heights[right]:
                    right-=1
        return maximum
