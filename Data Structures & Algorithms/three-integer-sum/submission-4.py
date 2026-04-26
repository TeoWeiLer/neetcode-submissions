class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # hash map 
        nums.sort() # to organize duplicates and allow easy skipping
        count = defaultdict(int) # freq map, serves as the extra space
        for num in nums:
            count[num] += 1
        
        res = []
        for i in range(len(nums)): # loop through each index i
            count[nums[i]] -= 1 # decrease count of nums[i] so it wont be reused
            if i and nums[i] == nums[i - 1]: # skipping duplicates
                continue

            for j in range(i + 1, len(nums)): # loop through index j>i
                count[nums[j]] -= 1 # decrease count
                if j - 1 > i and nums[j] == nums[j - 1]: # skipping duplicates
                    continue
                
                target = -(nums[i] + nums[j]) # computing k
                if count[target] > 0:
                    res.append([nums[i], nums[j], target])

            for j in range(i + 1, len(nums)): 
                count[nums[j]] += 1
                # after finishing all j, restore the counts for the second loop 
                # add back all the decremented values
                # so that it can be reused for the next i

        return res
        # O(n^2) since nested loop of i and j