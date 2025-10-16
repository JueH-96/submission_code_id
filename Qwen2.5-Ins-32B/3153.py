from typing import List

class Solution:
    def maxSum(self, nums: List[int], k: int) -> int:
        MOD = 10**9 + 7
        bit_count = [0] * 32
        
        for num in nums:
            for bit in range(32):
                if num & (1 << bit):
                    bit_count[bit] += 1
        
        result = 0
        for _ in range(k):
            current_num = 0
            for bit in range(31, -1, -1):
                if bit_count[bit] > 0:
                    current_num |= (1 << bit)
                    bit_count[bit] -= 1
            result = (result + current_num * current_num) % MOD
        
        return result