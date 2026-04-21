class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        mp = defaultdict(int) 
        # When you ask a defaultdict(int) for a key that doesn't exist, it doesn't crash; instead, it automatically creates that key and assigns it a default value of 0.
        for i in range(len(numbers)):
            tmp = target - numbers[i]
            if tmp in mp: # keeps the dictionary clean
                # When you run if mp[tmp]:, if tmp isn't in the dictionary, defaultdict creates it and returns 0.
                # Since if 0: is False, the code simply moves on to the next line. It effectively treats "missing" and "index 0" the same way
                return [mp[tmp], i + 1]
            mp[numbers[i]] = i + 1
            # Because all your stored values are now 1 or greater, if mp[tmp]: will always evaluate to True when a match is found.
        return []