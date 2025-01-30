class Solution(object):
    def singleNumber(self, nums):
        
        count = {}

        for num in nums:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1

        for num in count:
            if count[num] == 1:
                return num
        

solution = Solution()
# nums = [2,2,1]
# nums = [4,2,4,2,1]
nums = [1]
print(solution.singleNumber(nums))
