class Solution:
    def maxIncreasingGroups(self, usageLimits: List[int]) -> int:
        usageLimits.sort(reverse=True)
        total = 0
        groups = 0
        
        while usageLimits:
            groups += 1
            current_group_size = groups
            for i in range(current_group_size):
                if not usageLimits:
                    return groups - 1
                if usageLimits[-1] > 0:
                    usageLimits[-1] -= 1
                    if usageLimits[-1] == 0:
                        usageLimits.pop()
                else:
                    usageLimits.pop()
            usageLimits.sort(reverse=True)
        
        return groups