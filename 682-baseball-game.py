import time


class Solution:
    def calPoints(self, operations: list[str]) -> int:
        print(operations)
        record = []

        for operation in operations:
            match operation:
                case "+":
                    print("Plus!")
                    record.append(record[-1] + record[-2])
                case "D":
                    print("Dee")
                    record.append(record[-1] * 2)
                case "C":
                    print("Cee")
                    record.pop()
                case _:
                    print(int(operation))
                    record.append(int(operation))
        print(sum(record))
        return 1


ops = ["1", "C"]

start_time = time.perf_counter_ns()
solution = Solution()
solution.calPoints(ops)
end_time = time.perf_counter_ns()
elapsed_time = (end_time - start_time) / 100000

print(f"Elapsed time: {elapsed_time}ms")
