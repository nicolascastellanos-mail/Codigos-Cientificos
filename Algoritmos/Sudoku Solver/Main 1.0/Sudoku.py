# 09 oct 19:29

def print_board(board):
  for row in board:
    print(" ".join(map(str, row)))

def is_valid_move(board, row, col, num):
  # Check row and column
  if num in board[row] or num in [board[i][col] for i in range(9)]:
    return False

  # Check subgrid
  subgrid_row, subgrid_col = 3 * (row // 3), 3 * (col // 3)
  for i in range(subgrid_row, subgrid_row + 3):
    for j in range(subgrid_col, subgrid_col + 3):
      if board[i][j] == num:
        return False

  return True

def solve_sudoku(board):
  for row in range(9):
    for col in range(9):
      if board[row][col] == 0:
        for num in range(1, 10):
          if is_valid_move(board, row, col, num):
            board[row][col] = num
            if solve_sudoku(board):
              return True
            board[row][col] = 0
        return False
  return True

def find_most_complete_subgrid(board):
  most_complete_subgrid = None
  max_completed_cells = -1

  for row_start in range(0, 9, 3):
    for col_start in range(0, 9, 3):
      subgrid = [board[i][col_start:col_start + 3] for i in range(row_start, row_start + 3)]
      completed_cells = sum(1 for row in subgrid for cell in row if cell != 0)

      if completed_cells > max_completed_cells:
        max_completed_cells = completed_cells
        most_complete_subgrid = subgrid

  return most_complete_subgrid

def find_missing_numbers_in_subgrid(board, subgrid):
  flat_subgrid = [num for row in subgrid for num in row]
  missing_numbers = set(range(1, 10)) - set(flat_subgrid)

  for num in missing_numbers:
    row_positions = []
    col_positions = []

    for row_idx, row in enumerate(subgrid):
      for col_idx, cell in enumerate(row):
        if cell == 0 and num not in board[row_idx]:
          row_positions.append(row_idx)
          col_positions.append(col_idx)

    if len(row_positions) == 1:
      return num, row_positions[0], col_positions[0]

  return None, None, None

def main():
  # Define your Sudoku board here (0 represents empty cells)
  board = [
    [8, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 3, 6, 0, 0, 0, 0, 0],
    [0, 7, 0, 0, 9, 0, 2, 0, 0],
    [0, 5, 0, 0, 0, 7, 0, 0, 0],
    [0, 0, 0, 0, 4, 5, 7, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 3, 0],
    [0, 0, 1, 0, 0, 0, 0, 6, 8],
    [0, 0, 8, 5, 0, 0, 0, 1, 0],
    [0, 9, 0, 0, 0, 0, 4, 0, 0]
  ]

  """
  Solution:
    8 1 2 7 5 3 6 4 9
    9 4 3 6 8 2 1 7 5
    6 7 5 4 9 1 2 8 3
    1 5 4 2 3 7 8 9 6
    3 6 9 8 4 5 7 2 1
    2 8 7 1 6 9 5 3 4
    5 2 1 9 7 4 3 6 8
    4 3 8 5 2 6 9 1 7
    7 9 6 3 1 8 4 5 2
  """


  print("Sudoku Puzzle:")
  print_board(board)
  print("\nSolving...\n")

  if solve_sudoku(board):
    print("Solved Sudoku:")
    print_board(board)
  else:
    print("No solution exists.")

if __name__ == "__main__":
  main()

# 09 oct 19:39