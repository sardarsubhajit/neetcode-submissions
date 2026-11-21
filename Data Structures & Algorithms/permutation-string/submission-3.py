class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        s1Count = {}
        for ch in s1:
            s1Count[ch] = 1 + s1Count.get(ch,0)
        
        window = {}
        l = 0
        matches = 0
        need = len(s1Count)

        for r in range(len(s2)):
            r_ch = s2[r]
            window[r_ch] = 1 + window.get(r_ch, 0)
            if r_ch in s1Count:
                if window[r_ch] == s1Count[r_ch]:
                    matches += 1
                elif window[r_ch] == s1Count[r_ch] + 1:
                    matches -= 1
            
            if r-l+1 > len(s1):
                l_ch = s2[l]
                window[l_ch] -= 1
                if l_ch in s1Count:
                    if window[l_ch] == s1Count[l_ch]:
                        matches += 1
                    elif window[l_ch] == s1Count[l_ch] - 1:
                        matches -= 1

                        
                if window[l_ch] == 0:
                    del window[l_ch]
                l += 1

            if matches == need:
                return True

        return False        