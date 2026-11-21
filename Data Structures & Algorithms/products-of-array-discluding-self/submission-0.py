class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        out = []
        pre = 1
        # calculating the prefix list
        for i in range(len(nums)):
            print(i)
            if i > 0:
                pre *= nums[i-1]
            out.append(pre)

        # calculating the final result by multiplying with prefix list
        post = 1
        for i in range(-1, -(len(nums)+1), -1):
            if i < -1:
                post *= nums[i+1]
            out[i] *= post
        
        return out