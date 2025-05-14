import time


class Solution:
    def toLowerCase(self, s: str) -> str:
        print(s)
        char_list = list(s)

        for i in range(len(char_list)):
            ascii = ord(char_list[i])
            if ascii >= 65 and ascii <= 90:
                char_list[i] = chr(ascii + 32)
            else:
                continue
        return "".join(char_list)


s = "LOEVEL"

start_time = time.perf_counter_ns()

solution = Solution()
solution.toLowerCase(s)
end_time = time.perf_counter_ns()
elapsed_time = (end_time - start_time) / 100000

print(f"Elapsed time: {elapsed_time: .2f}ms")
