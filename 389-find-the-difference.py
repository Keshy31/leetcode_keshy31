import time


class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        output = 0

        for i in range(len(s)):
        for i in range(len(t)):
            if i < len(s):
                output ^= ord(s[i])
            output ^= ord(t[i])
        print(chr(output))
        return chr(output)


s = "a"
t = "ea"

start_time = time.perf_counter_ns()
solution = Solution()
solution.findTheDifference(s, t)
end_time = time.perf_counter_ns()
elapsed_time = (end_time - start_time) / 100000

print(f"Elapsed time: {elapsed_time:.2f}ms")
