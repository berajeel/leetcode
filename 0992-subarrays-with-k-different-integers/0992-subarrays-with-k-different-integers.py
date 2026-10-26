# cook your dish here
class Solution(object):
    def subarraysWithKDistinct(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        return self.atMostK(nums, k) - self.atMostK(nums, k-1)
    
    def atMostK(self, nums, k):

        if k < 0:
            return 0

        left = 0
        count = {}
        total = 0

        for right in range(len(nums)):
            num = nums[right]
            count[num] = count.get(num, 0) + 1
            
            while len(count) > k:
                outgoing = nums[left]
                count[outgoing] -= 1 
                
                if count[outgoing] == 0:
                    del count[outgoing]
                
                left += 1 
            
            total += right - left + 1 
        
        return total