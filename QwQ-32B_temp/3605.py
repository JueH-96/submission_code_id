from typing import List

class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        ans = []
        for p in nums:
            found = -1
            for x in range(p):
                if (x | (x + 1)) == p:
                    found = x
                    break
            ans.append(found)
        return ans