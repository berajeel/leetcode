class Solution:
    def maxSubArray(self, nums) -> int:
        
        current = 0
        max_value = max(nums)
        
        for i in range(len(nums)):
            if current + nums[i] <0:
                current = 0
            else:
                current = current + nums[i]
                max_value = max(max_value, current)
        
        return max_value