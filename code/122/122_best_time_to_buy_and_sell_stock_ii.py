class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) == 0:
            return 0
        result = 0
        i = 0
        j = 1
        while j < len(prices):
            if prices[j] > prices[i]:
                result += prices[j] - prices[i]
            i +=1
            j +=1
        return result