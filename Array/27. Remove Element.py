class Solution():
    def removeElement(self, nums, val):
        
        k = 0

        if not nums:
            return 0
        
        for i in range(0, len(nums)):
            if (nums[i] != val):
                nums[k] = nums[i]
                k += 1

        return k


solution = Solution()
nums = [0,1,2,2,3,0,4,2]
val = 2
k = solution.removeElement(nums, val)
print(k)
print(nums[:k])

#Time Complexity - O(n)
#Space Complexity - O(1)