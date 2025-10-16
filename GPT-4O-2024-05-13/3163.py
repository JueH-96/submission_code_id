class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        n = len(nums)
        total_sum = 0
        
        for i in range(n):
            distinct_elements = set()
            for j in range(i, n):
                distinct_elements.add(nums[j])
                distinct_count = len(distinct_elements)
                total_sum += distinct_count ** 2
        
        return total_sum