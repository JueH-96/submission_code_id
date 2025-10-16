from typing import List

class Solution:
    def splitWordsBySeparator(self, words: List[str], separator: str) -> List[str]:
        result = []
        for word in words:
            split_word = word.split(separator)
            result.extend(filter(lambda x: x != "", split_word))
        return result