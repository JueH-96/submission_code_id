class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        left = 0
        max_length = 0
        freq = {}
        
        for right in range(len(nums)):
            # Add the current element to our frequency counter
            freq[nums[right]] = freq.get(nums[right], 0) + 1
            
            # If the frequency of the current element exceeds k,
            # we need to shrink the window from the left
            while freq[nums[right]] > k:
                freq[nums[left]] -= 1
                left += 1
            
            # Update the maximum length
            max_length = max(max_length, right - left + 1)
        
        return max_length