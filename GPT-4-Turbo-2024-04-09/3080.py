class Solution:
    def maxSubarrays(self, nums: List[int]) -> int:
        count = 0
        for num in nums:
            if num == 0:
                count += 1
        return count if count > 0 else 1