class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hash_map = [] # store values that have already appeared

        for i in nums:
            if i in hash_map:
                return True
            hash_map.append(i)
        return False
        # Time O(n), Space O(n)

        