class Solution(object):
    def reverseWords(self, s):
        
        s_list = s.split()
        sentence = s_list[::-1]
        
        return ' '.join(sentence)