class Solution(object):
    def longestSubstring(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        
        if len(s) < k:
            return 0
            
        window = {}
        
        for char in s:
            window[char] = window.get(char, 0) + 1
        
        for char in window:
            
            if window[char] < k:
                
                parts = s.split(char)
                
                return max(
                        self.longestSubstring(part, k)
                        for part in parts
                    )
        
        return len(s)