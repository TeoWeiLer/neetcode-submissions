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
        # .items() turns it into a list of tuples (number, count)
        # sorted by lambda function so sorted by x[1], 2nd element, count
        # reverse = True for the descending so most freq values at the start
        for i in range(k):
            res.append(sorted_items[i][0])
            # indexing into i, the most freq first, then 0 for the actual no. 
        
        return res