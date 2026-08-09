class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower()
        cleaned = ""
        for char in s:
            if char.isalnum():
                cleaned +=char
        if cleaned==cleaned[::-1]:
            return True
        return False

