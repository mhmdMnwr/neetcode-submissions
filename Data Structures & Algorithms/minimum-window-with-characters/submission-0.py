from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""
        
        # 1. Count what characters we need
        needed_chars = Counter(t)
        required_unique_matches = len(needed_chars)
        
        # 2. Track characters in our current sliding window
        window_counts = {}
        formed_unique_matches = 0
        
        # 3. Track the best answer found so far (length, left_index, right_index)
        ans = (float("inf"), None, None)
        
        l = 0
        # Move the right pointer to expand the window
        for r in range(len(s)):
            char = s[r]
            window_counts[char] = window_counts.get(char, 0) + 1
            
            # If the current character matches the required frequency in t
            if char in needed_chars and window_counts[char] == needed_chars[char]:
                formed_unique_matches += 1
            
            # Try to shrink the window from the left if it contains all of t
            while l <= r and formed_unique_matches == required_unique_matches:
                char_left = s[l]
                
                # Save the smallest window before shrinking
                if r - l + 1 < ans[0]:
                    ans = (r - l + 1, l, r)
                
                # The character at 'l' is leaving the window
                window_counts[char_left] -= 1
                if char_left in needed_chars and window_counts[char_left] < needed_chars[char_left]:
                    formed_unique_matches -= 1
                
                l += 1 # Shrink window
                
        # Return the smallest substring, or "" if no valid window was found
        return "" if ans[0] == float("inf") else s[ans[1] : ans[2] + 1]
