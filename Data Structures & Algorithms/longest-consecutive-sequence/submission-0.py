class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest_seq = 0

        for num in nums:
            if (num-1) not in numSet:   # if nums - 1 does not exist, we can create a seq.
                curr_seq = 1
                while (num + curr_seq) in numSet:
                    curr_seq += 1
                
                longest_seq = max(longest_seq, curr_seq)
            
        return longest_seq