class Solution:
    def stringMatching(self, words):
        output = []
        for i in range(len(words)):
            for j in range(len(words)):
                if i != j and words[i] in words[j]:
                    output.append(words[i])
                    break
        return output