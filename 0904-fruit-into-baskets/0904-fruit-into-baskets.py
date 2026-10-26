class Solution(object):
    def totalFruit(self, fruits):
        """
        :type fruits: List[int]
        :rtype: int
        """
        
        left = 0
        fruit_count = {}
        max_fruit = 0

        for right in range(len(fruits)):
            fruit = fruits[right]
            fruit_count[fruit] = fruit_count.get(fruit, 0) + 1

            while len(fruit_count) > 2:

                outgoing = fruits[left]
                fruit_count[outgoing] -= 1

                if fruit_count[outgoing] == 0:
                    del fruit_count[outgoing]
                left += 1

            window_length = right - left + 1
            max_fruit = max(max_fruit, window_length)

        
        return max_fruit