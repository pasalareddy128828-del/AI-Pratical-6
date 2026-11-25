
# N-Queens Problem using Backtracking

N = 4

board = [-1] * N

# Check whether placing a queen is safe
def is_safe(row, col):

    for i in range(row):

        # Check same column
        if board[i] == col:
            return False

        # Check diagonals
        if abs(board[i] - col) == abs(i - row):
            return False

    return True


# Backtracking function
def solve(row):

    if row == N:
        return True

    for col in range(N):

        if is_safe(row, col):

            board[row] = col

            if solve(row + 1):
                return True

            # Backtrack
            board[row] = -1

    return False


# Display the chessboard
if solve(0):

    print("Solution Found:\n")

    for i in range(N):
        for j in range(N):

            if board[i] == j:
                print("Q", end=" ")
            else:
                print(".", end=" ")

        print()

else:
    print("No solution exists")
