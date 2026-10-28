class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        current_max = nums[0]
        current_min = nums[0]
        max_product = nums[0]

        for i in range(1, len(nums)):

            num = nums[i]

            prev_max = current_max
            prev_min = current_min

            current_max = max(num, prev_max * num, prev_min * num)
            current_min = min(num, prev_max * num, prev_min * num)

            max_product = max(max_product, current_max)

        return max_product
        