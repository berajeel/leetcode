from collections import deque

class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        
        dq = deque()
        result = []

        for right in range(len(nums)):

            # Remove indicies outside the current window
            while dq and dq[0] <= right - k:
                dq.popleft()
            
            # Remove smaller or equal values from the back
            while dq and nums[dq[-1]] <= nums[right]:
                dq.pop()
            
            # Add the current index
            dq.append(right)

            # Record the maximum once the window is full
            if right >= k - 1:
                result.append(nums[dq[0]])
        
        return result

        

        