#TC O(n)
#SC O(n)

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        mstack = []
        res = [-1] * len(nums1)
        hm = {i:-1 for i in nums2}
        for i in range(len(nums2)):
            while len(mstack)!=0 and nums2[mstack[-1]]<nums2[i]:
                hm[nums2[mstack[-1]]] = nums2[i]
                mstack.pop()
            mstack.append(i)
            
        for k,v in enumerate(nums1):
            res[k] = hm[v] 
        
        return res