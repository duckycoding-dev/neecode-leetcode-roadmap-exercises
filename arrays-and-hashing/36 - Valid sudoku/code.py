# goal:

class Solution:
  def validSudoku(self, board: list[list[str]]) -> bool:

    hashRows = dict()
    hashCols = dict()
    hashQuadrant = dict()
    for indexRow, row in enumerate(board):
      for indexCol, value in enumerate(row):
        quadrant = (indexCol / 3).__floor__() + ((indexRow / 3).__floor__() * 3)
        if(value != '.'):
          if(hashRows.get(indexRow) == None):
            hashRows[indexRow] = [0]*(9)
          if(hashCols.get(indexCol) == None):
            hashCols[indexCol] = [0]*(9)
          if(hashQuadrant.get(quadrant) == None):
            hashQuadrant[quadrant] = [0]*(9)
          if(hashRows.get(indexRow)[int(value)-1] == 1 or hashCols.get(indexCol)[int(value)-1] == 1 or hashQuadrant.get(quadrant)[int(value)-1]):
            return False
          hashRows.get(indexRow)[int(value)-1] = hashRows.get(indexRow)[int(value)-1] + 1
          hashCols.get(indexCol)[int(value)-1] = hashCols.get(indexCol)[int(value)-1] + 1
          hashQuadrant.get(quadrant)[int(value)-1] = hashQuadrant.get(quadrant)[int(value)-1] + 1
        # print('cols',hashCols.get(indexCol))
        # print('quadrant',hashQuadrant.get(quadrant))
      # print('rows',hashRows.get(indexRow))
    return True
  



sudokuBoard1 = [
  ["5","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  [".",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"],
]

sudokuBoard2 = [
  ["8","3",".",".","7",".",".",".","."],
  ["6",".",".","2","1","9","5",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  [".",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"],
]

sudokuBoard3 = [
  [".","8","7","6","5","4","3","2","1"],
  ["2",".",".",".",".",".",".",".","."],
  ["3",".",".",".",".",".",".",".","."],
  ["4",".",".",".",".",".",".",".","."],
  ["5",".",".",".",".",".",".",".","."],
  ["6",".",".",".",".",".",".",".","."],
  ["7",".",".",".",".",".",".",".","."],
  ["8",".",".",".",".",".",".",".","."],
  ["9",".",".",".",".",".",".",".","."]
]

submit = Solution()
print(submit.validSudoku(sudokuBoard1)) # True
print(submit.validSudoku(sudokuBoard2)) # False
print(submit.validSudoku(sudokuBoard3)) # True
