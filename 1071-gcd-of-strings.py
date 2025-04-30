import time


class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1 + str2 != str2 + str1:
            return ""
        len1 = len(str1)
        len2 = len(str2)

        def gcd(len1: int, len2: int):
            while len2:
                len1, len2 = len2, len1 % len2
            return len1

        return str1[: gcd(len1, len2)]


str1 = "ABCABC"
str2 = "ABC"

solution = Solution()

start_time = time.perf_counter_ns()
solution.gcdOfStrings(str1, str2)
end_time = time.perf_counter_ns()

elapsed_time = (end_time - start_time) / 100000

print(f"Execution time: {elapsed_time:.3f} milliseconds")
