class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned = "".join(char.lower() for char in s if char.isalnum())
        length=len(cleaned)
        i=0
        j=length - 1
        while i < j:
            if cleaned[i]!=cleaned[j]: return False
            j-=1
            i+=1
        return True