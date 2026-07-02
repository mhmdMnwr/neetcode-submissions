class Solution:
    def isValid(self, s: str) -> bool:
        def matches(test: str, char: str) -> bool:
            if (test == '(' and char == ')') or (test == '[' and char == ']') or (test == '{' and char == '}'):
                return True
            else: 
                return False
                
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
                if not matches(test, char): 
                    return False
                    
        return len(stack) == 0
