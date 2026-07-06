from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hashMap = defaultdict(int)
        left = 0
        max_length = 0
        biggest_value = 0  # Tracks the highest frequency in the CURRENT window
        
        for right in range(len(s)):
            # 1. Add the current character to the window
            hashMap[s[right]] += 1
            
            # 2. Update the highest character frequency seen in the current window
            biggest_value = max(biggest_value, hashMap[s[right]])
            
            # Current window size is (right - left + 1)
            # 3. If (window size - biggest_value) > k, it means we need too many replacements.
            # So, shrink the window from the left.
            while (right - left + 1) - biggest_value > k:
                hashMap[s[left]] -= 1
                left += 1  # Move left pointer forward
            
            # 4. Update the maximum length found so far
            max_length = max(max_length, right - left + 1)
            
        return max_length
