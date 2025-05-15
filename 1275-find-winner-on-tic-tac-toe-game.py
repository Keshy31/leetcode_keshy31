import time


class Solution:
    def tictactoe(self, moves: list[list[int]]) -> str:
        print(moves)
        board = [[""] * 3 for _ in range(3)]
        print(board)
        playerA = True

        for r, c in moves:
            print(f"row: {r}")
            print(f"column: {c}")
            if playerA:
                board[r][c] = "X"
            else:
                board[r][c] = "O"
            playerA = not playerA
        print(board)

        for i in range(3):
            if board[i][0] and board[i][0] == board[i][1] == board[i][2]:
                return "A" if board[i][0] == "X" else "B"
            if board[0][i] and board[0][i] == board[1][i] == board[2][i]:
                return "A" if board[0][i] == "X" else "B"

        if board[0][0] and board[0][0] == board[1][1] == board[2][2]:
            return "A" if board[0][0] == "X" else "B"
        if board[0][2] and board[0][2] == board[1][1] == board[2][0]:
            return "A" if board[0][2] == "X" else "B"

        return "Draw" if len(moves) == 9 else "Pending"


moves = [[0, 0], [1, 1], [2, 0], [1, 0], [1, 2], [2, 1], [0, 1], [0, 2], [2, 2]]

start_time = time.perf_counter_ns()
solution = Solution()
print(solution.tictactoe(moves))
end_time = time.perf_counter_ns()
elapsed_time = (end_time - start_time) / 100000

print(f"Elapsed time: {elapsed_time}ms")
