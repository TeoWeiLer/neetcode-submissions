class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0

        for num in set(nums):
            if (num-1) not in set(nums):
                length = 1
                while (num+length) in set(nums):
                    length += 1
                longest = max(longest, length)

        return longest
        