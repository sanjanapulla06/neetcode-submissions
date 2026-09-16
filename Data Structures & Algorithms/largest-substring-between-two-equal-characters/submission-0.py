class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        first = {}
        ans = -1

        for i in range(len(s)):
            if s[i] in first:
                ans = max(ans, i - first[s[i]] - 1)
            else:
                first[s[i]] = i

        return ans