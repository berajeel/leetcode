class Solution(object):
    def maxSubarraySumCircular(self, nums):
        total = nums[0]

        current_max = nums[0]
        max_sum = nums[0]

        current_min = nums[0]
        min_sum = nums[0]

        for i in range(1, len(nums)):
            num = nums[i]

            # 1. Update total
            total += num 

            # 2. Update current maximum and max_sum
            current_max = max(num, current_max + num)
            max_sum = max(max_sum, current_max)

            # 3. Update current minimum and min_sum
            current_min = min(num, current_min + num)
            min_sum = min(min_sum, current_min)

        # 4. Handle the all-negative case
        if max_sum < 0:
            return max_sum

        # 5. Return the better of the normal and circular sums
        return max(max_sum, total - min_sum)
    
    