class Solution(object):
    def plusOne(self, digits):
        
        int_digits = int("".join(map(str, digits)))
        total = int_digits + 1

        res = list(map(int, str(total)))

        # to convert array to integer
        # result = 0 
        # for i in digits:
        #     result = result * 10 + i      
       
        return res
    

solution = Solution()
# digits = [1,2,3]
# digits = [4,3,2,1]
digits = [9]
print(solution.plusOne(digits))

# info: digits = [1,2,3] output: [1,2,4]
# loop through one by one add it and than separate it using the math divide and reminder than simply put it to the array
# Time Complexity - O(n)
# Space Complextiy - O(n)