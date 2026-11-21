class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:    # counting the frequencies of the numbers in nums list
            count[num] = count.get(num, 0) + 1
        
        # creating a nested list with freq. values as index of the list
        freq = [[] for i in range(len(nums) + 1)]
        for n, c in count.items():
            freq[c].append(n)

        # finding the top k most freq. elements
        res = []
        for i in range(len(freq)-1, 0, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res