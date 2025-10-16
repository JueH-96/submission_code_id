from collections import Counter
from typing import List

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        count = Counter(nums)
        operations = 0
        
        for value in count.values():
            if value < 2:
                return -1
            operations += value // 3
            if value % 3 != 0:
                operations += 1
        
        return operations