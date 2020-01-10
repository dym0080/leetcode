class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        slow, fast = n, n
        slow = self.bitSquareSum(slow)
        fast = self.bitSquareSum(fast)
        fast = self.bitSquareSum(fast)
        while slow != fast:
            slow = self.bitSquareSum(slow)
            fast = self.bitSquareSum(fast)
            fast = self.bitSquareSum(fast)
        return slow == 1
    
    def bitSquareSum(self, n):
        sum1 = 0
        while n > 0:
            bit = n % 10
            sum1 += bit * bit
            n = n // 10
        return sum1