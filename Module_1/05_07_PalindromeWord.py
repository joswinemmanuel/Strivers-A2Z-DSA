class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        word = ""
        for i in s:
            if i in "abcdefghijklmnopqrstuvwxyz0123456789":
                word += i
        return word == word[::-1]
