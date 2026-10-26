class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        
        left = 0
        min_count = float('inf')
        sum = 0
        
        for right in range(len(nums)):
            
            sum += nums[right]
            
            while sum >= target:
                window_length = right - left + 1
                min_count = min(min_count, window_length)
                sum -= nums[left]
                left += 1
            
        
        if min_count == float('inf'):
            return 0
        else:
            return min_count