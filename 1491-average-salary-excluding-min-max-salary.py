class Solution:
    def average(self, salary: list[int]) -> float:
        print(f"Salary = {salary}")
        total = sum(salary)
        print(f"Sum = {total}")
        minimum = min(salary)
        print(f"Min = {minimum}")
        maximum = max(salary)
        print(f"Max = {maximum}")
        length = len(salary)
        print(f"N = {length}")

        print(f"Result = {(total - minimum - maximum) / (length - 2)}")
        return 1.0


salary = [1000, 2000, 3000]

solution = Solution()
solution.average(salary)
