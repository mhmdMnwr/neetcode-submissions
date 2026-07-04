class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack=[]
        result=[0]*len(temperatures)

        for i ,t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                _ , stacki = stack.pop()
                result[stacki]= i - stacki
            stack.append((t,i))
        return result
        