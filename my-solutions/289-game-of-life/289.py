class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        length = len(board)
        width = len(board[0])
        result = [[-1 for x in range(width)] for y in range(length)]

        def count_1(i, j):
            positions = [[i+1,j], [i-1,j], [i, j+1], [i, j-1], [i+1,j+1], [i-1,j-1], [i+1,j-1], [i-1,j+1]]

            num_1 = 0

            for x, y in positions:
                if length - 1 >= x >= 0 and width - 1 >= y >= 0 and board[x][y] == 1:
                    num_1 += 1

            return num_1

        for i in range(length):
            for j in range(width):
                num_1 = count_1(i, j)
                if board[i][j] == 1:
                    if num_1 < 2:
                        result[i][j] = 0
                    elif num_1 == 2 or num_1 == 3:
                        result[i][j] = 1
                    elif num_1 > 3:
                        result[i][j] = 0
                    else:
                        result[i][j] = board[i][j]
                elif board[i][j] == 0:
                    if num_1 == 3:
                        result[i][j] = 1
                    else:
                        result[i][j] = board[i][j]

        for i in range(length):
            for j in range(width):
                board[i][j] = result[i][j]
