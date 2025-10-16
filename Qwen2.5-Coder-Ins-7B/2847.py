class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        word_set = set(words)
        count = 0
        for word in words:
            reversed_word = word[::-1]
            if reversed_word in word_set and reversed_word != word:
                count += 1
                word_set.remove(word)
                word_set.remove(reversed_word)
        return count // 2