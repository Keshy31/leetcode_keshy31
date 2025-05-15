import time


class Solution:
    def judgeCircle(self, moves: str) -> bool:
        print(moves)
        lr_position = 0
        ud_position = 0
        for move in moves:
            print(move)
            match move:
                case "U":
                    ud_position += 1
                case "D":
                    ud_position -= 1
                case "R":
                    lr_position += 1
                case "L":
                    lr_position -= 1
        print(ud_position + lr_position)

        return ud_position == 0 and lr_position == 0


moves = "UD"

start_time = time.perf_counter_ns()
solution = Solution()
solution.judgeCircle(moves)
end_time = time.perf_counter_ns()
elapsed_time = (end_time - start_time) / 100000

print(f"Elapsed time: {elapsed_time}ms")
