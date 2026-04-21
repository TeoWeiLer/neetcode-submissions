class Solution: # bubble sort solution
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        # hashmap to count occurances of each value
        freq = [[] for i in range(len(nums)+1)] 
        # initialise empty frequency buckets of same size as nums input
        # +1 is to account for 0 in the array

        for num in nums:
            count[num] = count.get(num, 0) + 1 
            # .get takes in a key, 0 is the default if no value
        for num, cnt in count.items():
        # .items turns it into a view of a list of tuples
            freq[cnt].append(num)

        res = []
        for i in range(len(freq) - 1, 0, -1): 
            # range starting from total length of nums (not including 0), to 0, 
            # -1 increments for descending order 
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res