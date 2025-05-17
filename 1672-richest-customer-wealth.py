import time


class Solution:
    def maximumWealth(self, accounts: list[list[int]]) -> int:
        print(accounts)
        maximum = 0

        for customer in accounts:
            total = sum(customer)
            print(total)
            if total > maximum:
                maximum = total

        print(maximum)

        return maximum


accounts = [[2, 8, 7], [7, 1, 3], [1, 9, 5]]
solution = Solution()

start_time = time.perf_counter_ns()
solution.maximumWealth(accounts)
end_time = time.perf_counter_ns()

elapsed_time = (end_time - start_time) / 100000

print(f"Execution time: {elapsed_time:.3f} milliseconds")
