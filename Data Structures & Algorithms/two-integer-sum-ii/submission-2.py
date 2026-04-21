class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1
        if numbers[l] + numbers[r] == target:
                    return [l+1, r+1]
        # even when adding smallest with largest, still exceed the target
        while numbers[l] + numbers[r] != target:
            while numbers[l] + numbers[r] > target: 
                r -= 1 # decrement right pointer
                if numbers[l] + numbers[r] == target:
                    return [l+1, r+1]
            while numbers[l] + numbers[r] < target: 
                l += 1 # else increment the left pointer
                if numbers[l] + numbers[r] == target:
                    return [l+1, r+1]
        
