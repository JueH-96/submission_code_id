class Solution:
    def countWays(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        count = 0
        
        # Check if selecting 0 students makes everyone happy
        if nums[0] > 0:
            count += 1
        
        # Check for each possible number of selected students
        for i in range(n):
            # If the current number of selected students is i + 1
            # Check if nums[i] < i + 1 and (i == n-1 or nums[i+1] > i + 1)
            if nums[i] < i + 1 and (i == n - 1 or nums[i + 1] > i + 1):
                count += 1
        
        return count