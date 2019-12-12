# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        left, right = 1, n
        while left <= right:
            mid = (left + right) // 2
            temp = guess(mid)  # call API
            if temp == 0:
                return mid
            elif temp == -1:
                right = mid - 1               
            else:
                left = mid + 1        
        return -1





# 解决 pylint 在vscode中检测出的报错，定义一个假的API
def guess(num):
    return 0 
