class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        left = 0
        right = len(nums) - 1
        index = len(nums) - 1
        result = len(nums) * [0]
        current = 0

        while left <= right:

            if abs(nums[left]) > abs(nums[right]):
                current = nums[left] * nums[left]
                result[index] = current
                left += 1
                index -= 1
            else:
                current = nums[right] * nums[right]
                result[index] = current
                right -= 1
                index -= 1 

        return result