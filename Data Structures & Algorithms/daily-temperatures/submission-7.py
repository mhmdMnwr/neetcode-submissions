class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        numberOfDays=0
        result=[]
        for i in range(len(temperatures)):
            j=i+1
            while j < len(temperatures) :
                
                if temperatures[j]>temperatures[i]:
                    break
                else: numberOfDays+=1
                j+=1
            if j == len(temperatures): result.append(0)
            else:
                result.append(numberOfDays+1)
            numberOfDays=0
        return result
        