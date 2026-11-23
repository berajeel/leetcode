class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        
        if not s or not words:
            return []
            
        word_length = len(words[0])
        word_count = len(words)
        
        total_length = word_length * word_count
        
        if len(s) < total_length:
            return []
            
        word_freq = {}
        
        for word in words:
            word_freq[word] = word_freq.get(word, 0) + 1
        
        result = []
        
        for i in range(word_length):
            
            left = i
            window_count = {}
            count = 0
            
            for right in range(i, len(s) - word_length + 1, word_length):
                
                word = s[right:right + word_length]
                
                if word not in word_freq:
                    window_count.clear()
                    count = 0
                    left = right + word_length
                    continue
                
                window_count[word] = window_count.get(word, 0) + 1
                count += 1
                
                while window_count[word] > word_freq[word]:
                    
                    left_word = s[left:left + word_length]
                    
                    window_count[left_word] -= 1
                    count -= 1
                    left += word_length
                
                if count == word_count:
                    result.append(left)
        
        return result
                    
                    