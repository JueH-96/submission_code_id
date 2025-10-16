class Solution:
    def maximumStrongPairXor(self, nums: List[int]) -> int:
        max_xor = 0
        n = len(nums)

        for i in range(n):
            for j in range(i, n):
                x, y = nums[i], nums[j]
                if abs(x - y) <= min(x, y):
                    max_xor = max(max_xor, x ^ y)

        return max_xor