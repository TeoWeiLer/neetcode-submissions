class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1
        # nature of the sorted array
        while l < r: 
            # even when adding smallest with largest, still exceed the target
            if numbers[l] + numbers[r] > target: 
                r -= 1 # decrement right pointer
            elif numbers[l] + numbers[r] < target: 
                l += 1 # else increment the left pointer
            else:
                return [l+1, r+1]