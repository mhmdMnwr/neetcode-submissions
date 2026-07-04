import operator
from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operator_mapping = {
            "+": operator.add,
            "-": operator.sub,
            "*": operator.mul,
            "/": lambda a, b: int(a / b)  
        }
        
        stack = []
        
        for token in tokens:
            if token in operator_mapping:
                a=stack.pop()
                b=stack.pop()
                result=operator_mapping[token](b,a)
                stack.append(result)
            else: stack.append(int(token))
        return stack[0]
        

        


