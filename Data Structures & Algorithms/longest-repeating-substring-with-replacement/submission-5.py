from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hashMap = defaultdict(int)
        left = 0
        max_length = 0
        biggest_value = 0  
        
        for right in range(len(s)):
            hashMap[s[right]] += 1
            
            biggest_value = max(biggest_value, hashMap[s[right]])
            
            while (right - left + 1) - biggest_value > k:
                hashMap[s[left]] -= 1
                left += 1  
            
            max_length = max(max_length, right - left + 1)
            
        return max_length
