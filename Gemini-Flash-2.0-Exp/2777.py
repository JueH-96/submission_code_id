class Solution:
    def distinctDifferenceArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        diff = []
        for i in range(n):
            prefix = nums[:i+1]
            suffix = nums[i+1:]
            
            distinct_prefix = len(set(prefix))
            distinct_suffix = len(set(suffix))
            
            diff.append(distinct_prefix - distinct_suffix)
        
        return diff