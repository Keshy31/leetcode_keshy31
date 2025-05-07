import time


class Solution:
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
        print(flowerbed)
        if not n:
            return True

        p = 0

        while p < len(flowerbed):
            if p == 0:
                prev = 0
            else:
                prev = flowerbed[p - 1]

            curr = flowerbed[p]
            if p == len(flowerbed) - 1:
                next = 0
            else:
                next = flowerbed[p + 1]

            if (curr + prev + next) == 0:
                flowerbed[p] = 1
                n -= 1
            if n == 0:
                return True
            p += 1
        return False


flowerbed = [0]
n = 1

start_time = time.perf_counter_ns()
solution = Solution()
print(solution.canPlaceFlowers(flowerbed, n))
end_time = time.perf_counter_ns()
elapsed_time = (end_time - start_time) / 100000
print(f"Elapsed time: {elapsed_time:.2f}ms")
