class Solution:
    def minWindow(self, s: str, t: str) -> str:
        tCount = {}
        for ch in t:
            tCount[ch] = 1 + tCount.get(ch, 0)
        
        window = {}
        res, resLen = [-1, -1], float('inf')
        have, need = 0, len(tCount)
        l = 0
        for r in range(len(s)):
            r_ch = s[r]
            if r_ch in tCount:
                window[r_ch] = 1 + window.get(r_ch, 0)
                if window[r_ch] == tCount[r_ch]:
                    have += 1
            
            while have == need:
                # update the result
                if (r-l+1) < resLen:
                    res = [l, r]
                    resLen = (r-l+1)

                # remove a char from the left of the window
                l_ch = s[l]
                if l_ch in tCount:
                    window[l_ch] -= 1
                    if window[l_ch] < tCount[l_ch]:
                        have -= 1

                l += 1
        
        return s[res[0]: res[1]+1]