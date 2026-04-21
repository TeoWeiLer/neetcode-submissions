class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)
        # without using extra prefix and suffix arrays

        # first pass: fill res[i] with the product of all elements to the left of i (prefix product)
        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
        # second pass, multiply each res[i] with the product of all elements to the right of i (postfix product)    
        postfix = 1
        for i in range(len(nums) -1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]

        return res