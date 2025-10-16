class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        n = len(nums)
        total_sum = 0
        
        for i in range(n):
            seen = {}
            for j in range(i, n):
                if nums[j] in seen:
                    seen[nums[j]] += 1
                else:
                    seen[nums[j]] = 1
                distinct_count = len(seen)
                total_sum += distinct_count ** 2
        
        return total_sum