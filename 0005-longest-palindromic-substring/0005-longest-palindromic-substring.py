class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        result = ""

        def expandcenter(left, right):
            
            while (left >= 0 and right < len(s) and s[left] == s[right]):
                left -= 1
                right += 1
            
            return left + 1, right - 1
        
        for i in range(len(s)):

            left1, right1 = expandcenter(i, i)

            left2, right2 = expandcenter(i, i+1)

            if right1 - left1 + 1 > len(result):
                result = s[left1:right1 + 1]
            
            if right2 - left2 + 1 > len(result):
                result = s[left2:right2 + 1]
        
        return result
