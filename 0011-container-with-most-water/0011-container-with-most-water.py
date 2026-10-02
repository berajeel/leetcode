class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        left = 0 
        right = len(height) - 1
        answer = 0
        
        while left < right:

            width = right - left
            container_height = min(height[left], height[right])
            area = width * container_height

            answer = max(answer, area)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        
        return answer