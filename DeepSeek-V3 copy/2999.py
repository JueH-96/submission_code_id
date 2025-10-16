class Solution:
    def canBeEqual(self, s1: str, s2: str) -> bool:
        # Check if the characters at even indices are the same in both strings
        even_s1 = sorted([s1[0], s1[2]])
        even_s2 = sorted([s2[0], s2[2]])
        if even_s1 != even_s2:
            return False
        # Check if the characters at odd indices are the same in both strings
        odd_s1 = sorted([s1[1], s1[3]])
        odd_s2 = sorted([s2[1], s2[3]])
        if odd_s1 != odd_s2:
            return False
        return True