from typing import List  

class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        if len(strs) == 0: 
            return "empty"
        for i in strs:
            result += f"{len(i)}#{i}"
        return result

    def decode(self, s: str) -> List[str]:
        if s=="empty":return[]
        result = []
        number = 0
        stringNumber="0"
        
        i = 0
        while i < len(s):
            stringNumber="0"
            while s[i]!="#":
                stringNumber+=s[i]
                i+=1
            number = int(stringNumber)
            j = i + 1 + number
            result.append(s[i+1 : j]) 
            if (j + 1) < len(s):
                i = j  
            else:
                break
                
        return result