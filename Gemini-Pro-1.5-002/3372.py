class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 1:
            return n
        
        inc = 1
        dec = 1
        ans = 1
        
        for i in range(1, n):
            if nums[i] > nums[i-1]:
                inc += 1
                dec = 1
            elif nums[i] < nums[i-1]:
                dec += 1
                inc = 1
            else:
                inc = 1
                dec = 1
            ans = max(ans, inc, dec)
            
        return ans