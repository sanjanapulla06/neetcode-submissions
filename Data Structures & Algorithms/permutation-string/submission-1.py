class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        else:
            count_s1 = [0] * 26
            for c in s1:
                count_s1[ord(c) - ord('a')] += 1
            count_window = [0] * 26
            for c in s2[:len(s1)]:
                count_window[ord(c) - ord('a')] += 1
            if count_s1 == count_window:
                return True
            for right in range(len(s1), len(s2)):
                count_window[ord(s2[right]) - ord('a')] += 1        
                count_window[ord(s2[right - len(s1)]) - ord('a')] -= 1  
                if count_s1 == count_window:
                    return True
        return False
