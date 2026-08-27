"""
class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean = ""

        for c in s:
            if c.isalnum():
                clean += c.lower()

        return clean == clean[::-1]
"""

class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1

        while left < right:
            if left < right and not self.isAlpnum(s[left]):
                left += 1
                continue

            if left < right and not self.isAlpnum(s[right]):
                right -= 1
                continue

            if s[left].lower() != s[right].lower():
                return False
            
            left, right = left + 1, right - 1
        return True

    def isAlpnum(self, c):
        return (ord("A") <= ord(c) <= ord("Z") or
                ord("a") <= ord(c) <= ord("z") or
                ord("0") <= ord(c) <= ord("9"))