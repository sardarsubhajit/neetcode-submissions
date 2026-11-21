class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        freq_s = {}
        for ch in s:
            freq_s[ch] = freq_s.get(ch, 0) + 1
        
        for ch in set(t):
            if ch not in freq_s or t.count(ch) != freq_s[ch]:
                return False

        return True