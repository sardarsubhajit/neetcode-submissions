class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        tempstack = [] # will be storing pair of [temp, indx]

        # for i in range(len(temperatures)):
        #     while tempstack and temperatures[i] > tempstack[-1][0]:
        #         _, indx = tempstack.pop()
        #         res[indx] = (i - indx)
        #     tempstack.append([temperatures[i], i])

        for i, t in enumerate(temperatures):
            while tempstack and t > tempstack[-1][0]:
                _, indx = tempstack.pop()
                res[indx] = (i-indx)
            tempstack.append([t, i])
        
        return res