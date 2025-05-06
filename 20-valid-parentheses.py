import time


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        if s[0] in {")", "}", "]"}:
            return False
        for i in range(len(s)):
            if s[i] in {"(", "{", "["}:
                stack.append(s[i])
            elif s[i] == ")":
                if stack.pop() != "(":
                    return False
            elif s[i] == "}":
                if stack.pop() != "{":
                    return False
            elif s[i] == "]":
                if stack.pop() != "[":
                    return False
            print(stack)

        if stack:
            return False

        return True


s = "]"

start_time = time.perf_counter_ns()
solution = Solution()
solution.isValid(s)
end_time = time.perf_counter_ns()
elapsed_time = (end_time - start_time) / 100000

print(f"Elapsed time: {elapsed_time:.2f}ms")
