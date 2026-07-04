class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        maxArea=0
        width=1
        for i in range(len(heights)):
            width=1
            for j in range(i+1,len(heights)):
                if heights[j]<heights[i]: break
                else: width+=1
            for k in range(i-1 , -1, -1):
                if heights[k]<heights[i]: break
                else: width+=1
            maxArea=max(maxArea, heights[i]*width)
        return maxArea