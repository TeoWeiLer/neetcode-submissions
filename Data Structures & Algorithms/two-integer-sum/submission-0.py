class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        hash_map = {}

        for i, num in enumerate(nums):
            difference = target - nums[i]

            if difference in hash_map:
                return [hash_map[difference], i]
            else:
                hash_map[num] = i
        