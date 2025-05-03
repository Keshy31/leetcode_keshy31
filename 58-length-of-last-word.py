import time


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        isLastWord = True
        lastWordLength = 0
        p = len(s) - 1
        trimNeeded = True
        print(p)

        while trimNeeded:
            if s[p] == " ":
                p -= 1
            else:
                trimNeeded = False

        while isLastWord and p >= 0:
            print(s[p])
            if s[p] == " ":
                isLastWord = False
            else:
                lastWordLength += 1
                p -= 1
        print(lastWordLength)
        return lastWordLength


s = "world"
solution = Solution()

start_time = time.perf_counter_ns()

solution.lengthOfLastWord(s)

end_time = time.perf_counter_ns()

elapsed_time = (end_time - start_time) / 100000

print(f"Execution time: {elapsed_time:.2f} milliseconds")
