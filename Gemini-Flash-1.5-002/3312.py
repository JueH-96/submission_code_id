class Solution:
    def countKeyChanges(self, s: str) -> int:
        if not s:
            return 0
        count = 0
        last_key = s[0].lower()
        for i in range(1, len(s)):
            current_key = s[i].lower()
            if current_key != last_key:
                count += 1
                last_key = current_key
        return count