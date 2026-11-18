class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        
        if len(s2) < len(s1):
            return False
            
        window_count = {}
        window_s = {}
        
        left = 0
        
        for char in s1:
            window_s[char] = window_s.get(char, 0) + 1
        
        for right in range(len(s2)):
            
            char = s2[right]
            window_count[char] = window_count.get(char, 0) + 1
            
            while right - left + 1 > len(s1):
                
                left_char = s2[left]
                window_count[left_char] -= 1
                
                if window_count[left_char] == 0:
                    del window_count[left_char]
                    
                left += 1
            
            if window_count == window_s:
                return True
        
        return False
            