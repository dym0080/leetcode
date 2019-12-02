class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        result = 0
        if x >= 0:
            temp1 = str(x)[::-1] 
            result = int(temp1)
        else:
            temp2 = str(-1*x)[::-1]
            result = -1 * int(temp2)
        
        if not -pow(2, 31) <= result <= pow(2, 31) - 1:
            return 0
        else:
            return result
        