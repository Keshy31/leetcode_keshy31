import time


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        print(haystack)
        print(needle)
        if haystack == needle:
            return 0
        for i in range(len(haystack) - len(needle) + 1):
            print(i)
            if haystack[i : i + len(needle)] == needle:
                return i

        return -1


haystack = "abc"
needle = "c"

start_time = time.perf_counter_ns()
solution = Solution()
solution.strStr(haystack, needle)
end_time = time.perf_counter_ns()
elapsed_time = (end_time - start_time) / 100000

print(f"Execution time: {elapsed_time:.2f} milliseconds")
