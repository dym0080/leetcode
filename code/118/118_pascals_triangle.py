class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        
        if numRows ==0: return []
        result = [[0]*n for n in range(1,numRows+1)] 
        for n in range(numRows):
            if n ==0:
                result[n] = [1]
            else:
                for i in range(n+1):
                    if i ==0 or i == n:
                        result[n][i] = 1
                    else:
                        result[n][i] = result[n-1][i-1] +result[n-1][i]
             
        return result