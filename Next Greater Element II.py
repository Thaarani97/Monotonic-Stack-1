#TC O(n)
#SC O(n)

class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        mstack = []
        res = [-1] * len(nums)
        for i in range(2*len(nums)):
            while len(mstack)!=0 and nums[mstack[-1]]<nums[i%len(nums)]:
                res[mstack[-1]] = nums[i%len(nums)]
                mstack.pop()
            
            if i < len(nums):
                mstack.append(i)
                
        return res