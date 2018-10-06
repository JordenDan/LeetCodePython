class Solution:
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        checkLst = board
        boxLst = [[] for _ in range(9)]
        for col in range(9):
            rowLst = []
            colIdx = col // 3
            for row in range(9):
                rowIdx = row // 3
                val = board[row][col]
                (boxLst[rowIdx * 3 + colIdx]).append(val)
                rowLst.append(val)
            checkLst.append(rowLst)
        checkLst += boxLst

        for checkItem in checkLst:
            if self.isInvalidItem(checkItem):
                return False
        return True

    def isInvalidItem(self, checkItem):
        valSet = set()
        for item in checkItem:
            if item == ".":
                continue
            if item in valSet:
                return True
            valSet.add(item)