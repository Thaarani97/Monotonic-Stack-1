#TC O(n)
#SC O(n)

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        mstack = []
        for i in range(len(temperatures)):
            while len(mstack)!=0 and temperatures[i] > temperatures[mstack[-1]]:
                idx = i - mstack[-1]
                result[mstack[-1]] = idx
                mstack.pop()
            mstack.append(i)
        return result
        