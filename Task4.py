#Sudoko Puzzle
def display_sudoku(board):
    for row in board:
        print(" ".join(str(cell) if cell != 0 else '.' for cell in row))


def is_safe_to_place(board, row, col, num):
    if num in board[row]:
        return False
    for r in range(9):
        if board[r][col] == num:
            return False
    start_row, start_col = (row // 3) * 3, (col // 3) * 3
    for r in range(start_row, start_row + 3):
        for c in range(start_col, start_col + 3):
            if board[r][c] == num:
                return False

    return True


def solve(board):
    for r in range(9):
        for c in range(9):
            if board[r][c] == 0:  
                for num in range(1, 10):  
                    if is_safe_to_place(board, r, c, num):
                        board[r][c] = num  
                        if solve(board):  
                            return True
                        board[r][c] = 0  
                return False  
    return True  


def main():
    print("Enter the Sudoku puzzle (row by row), use 0 for empty cells:")
    sudoku_board = []
    for i in range(9):
        row = list(map(int, input(f"Enter row {i + 1}: ").split()))
        if len(row) != 9:
            print("Each row should contain exactly 9 numbers.")
            return
        sudoku_board.append(row)

    print("\nInitial Sudoku Puzzle:")
    display_sudoku(sudoku_board)

    if solve(sudoku_board):
        print("\nSolved Sudoku Puzzle:")
        display_sudoku(sudoku_board)
    else:
        print("\nNo solution found for this Sudoku puzzle.")


if __name__ == "__main__":
    main()
