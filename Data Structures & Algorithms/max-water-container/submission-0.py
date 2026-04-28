class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # two pointers, i at left, j at right
        i, j = 0, len(heights)-1
        max_water = 0 # store value for max area

        # always true for container to exist 
        while i<j:
            amt = (j-i) * min(heights[i], heights[j])
            max_water = max(amt, max_water) # update the max area so far
            # move the shorter height pointer
            if heights[i] <= heights[j]: 
                i += 1 
            else:
                j -= 1
        
        return max_water
