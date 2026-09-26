class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        freq = {}

        for c in chars:
            freq[c] = freq.get(c, 0) + 1

        total = 0

        for word in words:
            wordfreq = {}
            
            for c in word:
                wordfreq[c] = wordfreq.get(c, 0) + 1

            good = True

            for c in wordfreq:
                if wordfreq[c] > freq.get(c, 0):
                    good = False
                    break

            if good:
                total += len(word)

        return total