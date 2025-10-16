from typing import List
from functools import lru_cache

class Solution:
    def specialPerm(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(nums)
        
        @lru_cache(None)
        def dp(mask, last):
            if mask == (1 << n) - 1:
                return 1
            ans = 0
            for i in range(n):
                if ((mask >> i) & 1) == 0 and (last == -1 or nums[i] % nums[last] == 0 or nums[last] % nums[i] == 0):
                    ans = (ans + dp(mask | (1 << i), i)) % MOD
            return ans
        
        return dp(0, -1)