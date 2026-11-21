class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = list(filter(lambda ch: ch.isalnum(), list(s)))
        s = ''.join(s)
        s = s.lower()
        
        left, right = 0, len(s)-1
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True