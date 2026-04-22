class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()  # Sort in-place
        res = []

        # stops at len(nums) - 2 because you need at least two more numbers to form a triplet
        for i in range(len(nums) - 2): 
            # Skip the same element to avoid duplicate triplets
            # not including the first element
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            # starting from after i to be more efficient
            j, k = i + 1, len(nums) - 1
            
            while j < k:
                curSum = nums[i] + nums[j] + nums[k]
                
                if curSum < 0:
                    j += 1
                elif curSum > 0:
                    k -= 1
                else:
                    res.append([nums[i], nums[j], nums[k]])
                    
                    # Move pointers and skip duplicates for j and k
                    while j < k and nums[j] == nums[j + 1]: # move the pointer to the last instance of a duplicate value.
                        j += 1
                    while j < k and nums[k] == nums[k - 1]:
                        k -= 1
                        
                    j += 1 # moves the pointer to a new number
                    k -= 1

        return res