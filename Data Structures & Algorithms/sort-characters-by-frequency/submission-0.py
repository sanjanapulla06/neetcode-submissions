class Solution:
    def frequencySort(self, s: str) -> str:
        freq = {}

        for ch in s:
            freq[ch] = freq.get(ch, 0) + 1

        chars = sorted(freq, key=lambda ch: freq[ch], reverse=True)

        result = ""
        for ch in chars:
            result += ch * freq[ch]

        return result