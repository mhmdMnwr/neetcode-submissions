class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen=[]
        mx=0
        for char in s:
            if char in seen:
                index=seen.index(char)
                del seen[:index+1]
            seen.append(char)
            mx=max(mx,len(seen))
        return mx    