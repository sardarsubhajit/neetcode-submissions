class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0   # setup the left pointer
        res = 0     
        for r in range(len(s)): # setup the right pointer
            while l < r and s[r] in s[l:r]:     # shift the left pointer until duplicate exists in the visited sub-string
                l += 1
            res = max(res, r-l+1)
        
        return res