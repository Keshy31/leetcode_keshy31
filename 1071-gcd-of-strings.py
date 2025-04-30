import time


class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        print(str1)
        print(str2)

        for i in range(0, len(str2), 1):
            if str1[i] == str2[i]:
                print("true")

        return ""


str1 = "ABCABC"
str2 = "ABC"

solution = Solution()

start_time = time.perf_counter_ns()
solution.gcdOfStrings(str1, str2)
end_time = time.perf_counter_ns()

elapsed_time = (end_time - start_time) / 100000

print(f"Execution time: {elapsed_time:.2f} milliseconds")
