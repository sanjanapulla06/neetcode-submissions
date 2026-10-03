class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        res = []
        i = 0

        while i < len(words):
            line = []
            line_len = 0

            while i < len(words) and line_len + len(words[i]) + len(line) <= maxWidth:
                line.append(words[i])
                line_len += len(words[i])
                i += 1

            if i == len(words) or len(line) == 1:
                current = " ".join(line)
                current += " " * (maxWidth - len(current))
                res.append(current)

            else:
                spaces = maxWidth - line_len
                gaps = len(line) - 1

                space_each = spaces // gaps
                extra = spaces % gaps

                current = ""

                for j in range(gaps):
                    current += line[j]
                    current += " " * (space_each + (1 if j < extra else 0))

                current += line[-1]
                res.append(current)

        return res