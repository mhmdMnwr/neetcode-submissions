import numpy as np

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zeroCount=0
        product=1
        for num in nums:
            if num == 0:
                zeroCount+=1
            else: product = product*num
        result=[]
        if zeroCount>1: return [0]*len(nums)
        if zeroCount==0:
            for num in nums:
                result.append(product//num)
        else:
            for num in nums:
                if(num == 0):result.append(product)
                else: result.append(0)

        return result