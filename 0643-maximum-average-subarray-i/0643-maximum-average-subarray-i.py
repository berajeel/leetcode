class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        
        left = 0
        current_sum = 0

        for i in range(k):
            current_sum += nums[i]
        
        max_average = current_sum

        for right in range(k, len(nums)):

            current_sum = current_sum + nums[right] - nums[left]
            left += 1

            max_average = max(max_average, current_sum)
                    
        return float(max_average) / k
