from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output = defaultdict(list)

        for s in strs:
            count = [0] * 26    # creating the freq of each character from a...z
            for ch in s:
                count[ord(ch) - ord('a')] += 1  # counting frequencies
            
            output[tuple(count)].append(s)  # using the freq as the key in hashmap
            # since list can not be used as keys,we are type casting it as tuple
        
        return list(output.values())    # returning the values of the set