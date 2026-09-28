class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        freq = {}

        for word in words:
            for ch in word:
                freq[ch] = freq.get(ch, 0) + 1

        n = len(words)

        for ch in freq:
            if freq[ch] % n != 0:
                return False

        return True