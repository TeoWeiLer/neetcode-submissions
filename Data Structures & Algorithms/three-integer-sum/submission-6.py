class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # two pointers

        # sort -> handle duplicates & enable two pointer logic
        res = []
        nums.sort()

        # fix each number, others are two pointers
        for i, a in enumerate(nums): # looping through array
            # a = nums[i]
            # all remaining numbers are positive
            if a > 0: 
                break
            if i > 0 and a == nums[i - 1]: # skip duplicate values for first no.
                continue
            
            l, r = i + 1, len(nums) - 1
            while l < r: 
                threeSum = a + nums[l] + nums[r]
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else: 
                    res.append([a, nums[l], nums[r]])
                    # move both pointers inward, current pair is exhausted
                    # but might still have another pair for threeSum
                    l += 1
                    r -= 1
                    # skip duplicates at the left pointer, offset the sum
                    while nums[l] == nums[l - 1] and l < r:
                        # l<r here is to set the boundary so l is never > r
                        l += 1

        return res
            