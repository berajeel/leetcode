class Solution(object):
    def moveZeroes(self, nums):
        
        non_zero_index = 0
        
        for i in range(len(nums)):
            
            if nums[i] != 0:
                nums[non_zero_index] = nums[i]
                non_zero_index += 1

        for i in range(non_zero_index, len(nums)):
            nums[i] = 0

solution = Solution()
nums=[0,0,1]
# nums=[0,1,0,3,12]
solution.moveZeroes(nums)
print(nums)

#Time Complexity - O(n^2)
#Space Complexity - O(1)
        
# info: nums=[0,1,0,3,12]
# compare first and second element if zero found move 0 to the last element