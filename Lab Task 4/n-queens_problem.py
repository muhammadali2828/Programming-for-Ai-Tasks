def is_safe( board,row, col, n ):
      for i in range(col):
            if board[i] == row  or  abs(board[i] - row) == abs(i - col):
                return False
      return True

def solve_n_queens( board ,col ,n ):
      if col == n:
          print_board(board , n)
          return True  

      for row in range(n):
            if is_safe(board,row,col,n):
                  board[col] = row
                  if solve_n_queens( board , col + 1 , n ):
                        return True
                  board[col] = -1  
      return False  

def print_board( board , n ):
      for i in range(n):
            row_str = [ " Q " if board[j] == i else " . " for j in range(n)]
            print("   ".join(row_str))  
      print("\n")

def main():
      n = int(input(" Enter the size of the board .:  ")) 
      
      board = [-1] * n  

      if not solve_n_queens( board , 0 , n ):
          print(" No solution exists. ")

main()
