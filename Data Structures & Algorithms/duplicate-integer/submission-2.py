class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hash_map = [] 
        for i in nums:
            if i in hash_map:
                return True
            hash_map.append(i)
        return False

        