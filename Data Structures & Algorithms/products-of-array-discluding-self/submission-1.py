class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # division solution

        prod, zero_cnt = 1, 0
        for num in nums: # traversing array
            if num:
                prod *= num # multiply all non-zero numbers to get prod
            else:
                zero_cnt += 1 # counting no. of zeros
        if zero_cnt > 1: return [0] * len(nums) # zero_cnt > 1, return an array of all zeros

        res = [0] * len(nums) 
        for i, c in enumerate(nums):
            if zero_cnt: # one zero
                res[i] = 0 if c else prod # the index with the zero gets the prod of all non-zero numbers
            else: 
                res[i] = prod // c # no zeros, each result value is the division
        return res
        