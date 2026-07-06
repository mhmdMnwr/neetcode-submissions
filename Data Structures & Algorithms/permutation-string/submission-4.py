class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        sorted_string = "".join(sorted(s1))
        testingString=""
        for i in range(len(s2)):
            testingString=""
            if len(s2) >= i+len(s1):
             for j in range(i,i+len(s1)):
                
                testingString+=s2[j]
             testingString="".join(sorted(testingString))
             if testingString == sorted_string:return True
        return False