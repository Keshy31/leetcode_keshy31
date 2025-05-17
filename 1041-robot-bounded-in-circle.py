import time


class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        print(instructions)
        direction = "North"
        pos = [0, 0]

        for move in instructions:
            match direction:
                case "North":
                    if move == "G":
                        pos[1] += 1
                    elif move == "L":
                        direction = "West"
                    elif move == "R":
                        direction = "East"
                case "East":
                    if move == "G":
                        pos[0] += 1
                    elif move == "L":
                        direction = "North"
                    elif move == "R":
                        direction = "South"
                case "South":
                    if move == "G":
                        pos[1] -= 1
                    elif move == "L":
                        direction = "East"
                    elif move == "R":
                        direction = "West"
                case "West":
                    if move == "G":
                        pos[0] -= 1
                    elif move == "L":
                        direction = "South"
                    elif move == "R":
                        direction = "North"

        print(pos)
        print(direction)

        return True


instructions = "GG"

start_time = time.perf_counter_ns()
solution = Solution()
solution.isRobotBounded(instructions)
end_time = time.perf_counter_ns()
elapsed_time = (end_time - start_time) / 100000

print(f"Elapsed time: {elapsed_time}ms")
