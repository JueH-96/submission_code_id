from collections import Counter

class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        left = 0
        max_length = 0
        freq = Counter()
        
        for right in range(len(nums)):
            freq[nums[right]] += 1
            
            while freq[nums[right]] > k:
                freq[nums[left]] -= 1
                left += 1
                
            max_length = max(max_length, right - left + 1)
            
        return max_length