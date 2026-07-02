class MinStack:

    def __init__(self):
        self.stack=[]
        self.min= float('inf')
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.min=min(self.min , val)
        

    def pop(self) -> None:
        self.stack.pop()
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        mini=self.stack[0]
        for i in self.stack:
            value=i
            
            mini = min(mini,value)
        return mini
