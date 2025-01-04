class Solution():    
    def removeDuplicates(self, nums):
        
        # if the list is empty than return 0 
        if not nums:
            return 0

        # start with the second element
        k = 1

        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                nums[k] = nums[i]
                k += 1
                
        return k

solution = Solution()
nums = [1,1,2]
k = solution.removeDuplicates(nums)
print(k)
print(nums[:k])

# Time Complexity - O(n)
# Space Complexity - O(1)