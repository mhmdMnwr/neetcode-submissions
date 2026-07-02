class Solution:
    def isValid(self, s: str) -> bool:
        pattern = {"(":")" ,"[":"]" ,"{":"}" }
                
        stack = []
        if not s: 
            return True
        if s[0] == ")" or s[0] == "]" or s[0] == "}":
            return False
            
        for char in s:
            if char == "(" or char == "{" or char == "[":
                stack.append(char)
            else:
                if not stack: 
                    return False
                test = stack.pop(-1)
                if char != pattern[test]: 
                    return False
                    
        return len(stack) == 0
