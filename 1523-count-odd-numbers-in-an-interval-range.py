class Solution:
    def countOdds(self, low: int, high: int) -> int:
        print(f"Low = {low}")
        print(f"High = {high}")
        delta = high - low + 1
        print(f"delta = {delta}")

        if high % 2 != 0 and low % 2 != 0:
            print(delta / 2 + 1)
            return int(delta / 2) + 1
        print(int(delta / 2))
        return int(delta / 2)


low = 8
high = 11

solution = Solution()
solution.countOdds(low, high)
