class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for _ in range(len(nums) + 1)]

        for i in nums:
            count[i] = count.get(i, 0) + 1
        
        for i, cnt in count.items(): 
            freq[cnt].append(i) 
            # Use .append() so we don't overwrite numbers with the same frequency

        res = []
        for index in range(len(freq) -1, 0, -1):
            for value in freq[index]: 
                # freq[index] is now a list, so we iterate through it
                # handles multiple values in a bucket
                # this also ensures empty list values don't appear
                res.append(value)
                if len(res) == k:
                    return res
