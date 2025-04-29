import time


class Solution:
    def romanToInt(self, s: str) -> int:
        numeralMap = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        sum = 0
        sdd = list(s)
        prevNum = 0

        for i in range(len(s) - 1, -1, -1):
            currentNum = numeralMap[sdd[i]]
            if currentNum >= prevNum:
                sum += currentNum
            elif currentNum < prevNum:
                sum -= currentNum
            prevNum = currentNum
        return sum


s = "MCMXCIV"

start_time = time.perf_counter_ns()
solution = Solution()
solution.romanToInt(s)
end_time = time.perf_counter_ns()
elapsed_time = (end_time - start_time) / 100000

print(f"Execution time: {elapsed_time:.2f} milliseconds")
