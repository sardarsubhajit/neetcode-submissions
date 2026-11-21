class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        freq = {}
        for ch in s:    # counting the character frequnecy in string s
            freq[ch] = freq.get(ch, 0) + 1

        for ch in t:    # matching the character frequency in t wrt s
            if ch in freq and t.count(ch) == freq[ch]:
                continue
            else:
                return False
        
        return True
