class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        """ divide the length of array by 2
            compare if greater or smaller than the target
            go with the one that has the target
        """
        
        half = len(nums)//2
        print(half)
        
        if target == nums[0]:
            return 0
        
        elif target <= nums[half]:
            for i in range(half+1):
                if nums[i] == target:
                    return i
        
        elif target > nums[half]:
            for i in range(half, len(nums)):
                if nums[i] == target:
                    return i
        
        return -1
        
        