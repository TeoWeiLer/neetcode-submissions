class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash_map = {}
        res = []

        for i in nums:
            if i in hash_map:
                hash_map[i] += 1
            else:
                hash_map[i] = 1

        sorted_items = sorted(hash_map.items(), key=lambda x: x[1], reverse=True)
        for i in range(k):
            res.append(sorted_items[i][0])
        
        return res