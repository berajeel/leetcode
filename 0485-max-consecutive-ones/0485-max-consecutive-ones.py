class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        max_sum = 0
        current = 0

        for num in nums:
            if num == 1:
                current += 1
                max_sum = max(max_sum, current)
            else:
                current = 0
        return max_sum  

        # sum = 0
        # freq = {}

        # for i in range(len(nums)):
        #     if nums[i] == 1:
        #         freq[nums[i]] = freq.get(nums[i], 0) + 1
        #         sum += 1
        #         max_sum = max(max_sum, sum)
        #     else:
        #         max_sum = max(max_sum, sum)
        #         sum = 0
        #         del freq[1]
        
        
        