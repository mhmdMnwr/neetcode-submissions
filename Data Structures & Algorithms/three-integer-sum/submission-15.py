from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        output = []  # A list is enough now since we manually skip duplicates
        
        for i in range(len(nums)):
            # Optimization: If the current number is positive, 
            # three positive numbers can never sum to 0.
            if nums[i] > 0: 
                break
                
            # Skip duplicate values for the first element 'i'
            if i > 0 and nums[i] == nums[i - 1]:
                continue
                
            l = i + 1
            r = len(nums) - 1
            
            while l < r:
                current_sum = nums[i] + nums[l] + nums[r]
                
                if current_sum == 0:
                    output.append([nums[i], nums[l], nums[r]])
                    
                    # Move both pointers inward after finding a match
                    l += 1
                    r -= 1
                    
                    # Skip duplicate values for 'l' to avoid identical triplets
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                        
                    # Skip duplicate values for 'r' to avoid identical triplets
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1
                        
                elif current_sum > 0:
                    # The sum is too big, decrease the right pointer
                    r -= 1
                else:
                    # The sum is too small, increase the left pointer
                    l += 1
                    
        return output
