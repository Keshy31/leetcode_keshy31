import time


class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        if s in (s + s)[1:-1]:
            return True
        return False


s = "abab"

start_time = time.perf_counter_ns()

solution = Solution()
solution.repeatedSubstringPattern(s)
end_time = time.perf_counter_ns()
elapsed_time = (end_time - start_time) / 100000

print(f"Elapsed time: {elapsed_time: .2f}")
