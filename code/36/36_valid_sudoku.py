class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        temp3 = [[],[],[],[],[],[],[],[],[]]    # 粗实线分隔的 3x3 的数组    
        for i in range(9): 
            temp1 = []     # 1.数字 1-9 在每一行只能出现一次。    
            temp2 = []     # 2.数字 1-9 在每一列只能出现一次。
            for j in range(9):              
                if board[i][j] != '.' :                  
                    temp1.append(board[i][j])
                   
                if board[j][i] != '.' :
                    temp2.append(board[j][i])
            
            if i < 3:
                temp3[0] += board[i][0:3]
                temp3[1] += board[i][3:6]
                temp3[2] += board[i][6:9]
            elif i >=3 and i < 6:
                temp3[3] += board[i][0:3]
                temp3[4] += board[i][3:6]
                temp3[5] += board[i][6:9]
            else:
                temp3[6] += board[i][0:3]
                temp3[7] += board[i][3:6]
                temp3[8] += board[i][6:9]

            if  len(set(temp2)) < len(temp2) or len(set(temp1)) < len(temp1):
                return False
        for i in range(9):
            temp4 = [] # 数字 1-9 在每一个以粗实线分隔的 3x3 宫内只能出现一次。
            for j in range(9):
                if temp3[i][j] != '.' : 
                    temp4.append(temp3[i][j]) 
            if len(set(temp4)) < len(temp4):
                return False
        return True