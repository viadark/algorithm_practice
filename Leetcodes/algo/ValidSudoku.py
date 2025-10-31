class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        
        def isValidLine(line):
            chklist = list()
            for i in range(0, 10):
                chklist.append(0)
            for i in range(0, len(line)):
                if line[i] == '.':
                    continue
                if chklist[int(line[i])] != 0:
                    return False
                chklist[int(line[i])] = 1
            return True

        for i in range(0, 9):
            line = board[i][:]
            if not isValidLine(line):
                return False
            line = board[:][i]
            if not isValidLine(line):
                return False
        return True
s = Solution()
res = s.isValidSudoku([".87654321","22.......","3........","4........","5........","6........","7........","8........","9........"])
print("res = ", res)