class Solution(object):
    def findAnagrams(self, s, p):
        
        result = []
        
        if len(p) > len(s):
            return result
        
        p_count = {}
        window_count = {}
        left = 0
        
        for char in p:
            p_count[char] = p_count.get(char, 0) + 1
        
        for right in range(len(s)):
            
            char = s[right]
            window_count[char] = window_count.get(char, 0) + 1
            
            if right - left + 1 > len(p):
                
                left_char = s[left]
                window_count[left_char] -= 1
                
                if window_count[left_char] == 0:
                    del window_count[left_char]
                
                left += 1
            
            if right - left + 1 == len(p):
                
                if window_count == p_count:
                    result.append(left)
        
        return result
        
        
        