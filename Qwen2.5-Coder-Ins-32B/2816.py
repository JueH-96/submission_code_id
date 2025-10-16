class Solution:
    def makeSmallestPalindrome(self, s: str) -> str:
        s = list(s)
        left, right = 0, len(s) - 1
        while left < right:
            s[left] = s[right] = min(s[left], s[right])
            left += 1
            right -= 1
        return ''.join(s)