class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        temp3 = [[],[],[],[],[],[],[],[],[]]        
        for i in range(9): 
            temp1 = []         
            temp2 = []
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
            elif i>=6 and i < 9:
                temp3[6] += board[i][0:3]
                temp3[7] += board[i][3:6]
                temp3[8] += board[i][6:9]
            else:
                print("error")

            print("temp1-"+ str(i))    
            print(temp1)
            print("temp2-"+str(i))
            print(temp2)
            if  len(set(temp2)) < len(temp2) or len(set(temp1)) < len(temp1):
                return False
        
        print("temp3")
        print(temp3)
        for i in range(9):
            temp4 = []
            for j in range(9):
                if temp3[i][j] != '.' : 
                    temp4.append(temp3[i][j]) 
            print("temp4-"+str(i))
            print(temp4)
            if len(set(temp4)) < len(temp4):
                return False

        print("end")
        return True

            
ss = Solution()
board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
ss.isValidSudoku(board)