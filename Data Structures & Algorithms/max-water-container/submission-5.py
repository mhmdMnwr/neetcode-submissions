class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        maximum = 0
        
        while left < right:
            min_height = min(heights[left], heights[right])
            maximum = max(maximum, (right - left) * min_height)
            
            if heights[left] == min_height:
                # Keep moving right until you find a taller bar
                while left < right and heights[left] <= min_height:
                    left += 1
            else:
                # Keep moving left until you find a taller bar
                while left < right and heights[right] <= min_height:
                    right -= 1
                    
        return maximum
