class Solution(object):
    def maxAbsoluteSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        max_sum = nums[0]
        current_max = nums[0]
        
        min_sum = nums[0]
        current_min = nums[0]
        
        for i in range(1, len(nums)):
            num = nums[i]
            
            current_max = max(num, current_max + num)
            max_sum = max(max_sum, current_max)
            
            current_min = min(num, current_min + num)
            min_sum = min(min_sum, current_min)
            
        return max(max_sum, abs(min_sum))