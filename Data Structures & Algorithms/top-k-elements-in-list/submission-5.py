class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for _ in range(len(nums) + 1)]

        for i in nums:
            count[i] = count.get(i, 0) + 1
        for num, cnt in count.items():
            freq[cnt].append(num)
            # access the list of lists, append your values

        res = []
        for index in range(len(freq) - 1, 0, -1):
            for value in freq[index]: 
                # make sure to go through each list, possible multiple values in a list
                res.append(value)
                if len(res) == k:
                    return res




