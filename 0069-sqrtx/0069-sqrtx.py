class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        
        left = 0
        right = x 
        
        while left <= right:
            
            mid = (left + right) // 2
            result = mid * mid
            
            if result == x:
                return mid
            elif result < x:
                left = mid + 1
            else:
                right = mid - 1
        
        return right
               