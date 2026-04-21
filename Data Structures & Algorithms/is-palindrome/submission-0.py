class Solution:
    def isPalindrome(self, s: str) -> bool:
        # two pointers, left and right
        l, r = 0, len(s) - 1
        while l < r:
            while l < r and not s[l].isalnum(): # skip non-alphanumeric for left pointer
                l += 1
            while l < r and not s[r].isalnum(): # skip non-alphanumeric for right pointer
                r -= 1
            if s[l].lower() != s[r].lower(): # if condition for non-valid palindrome at all times
                return False
            # continuing to move the pointers if there are no issues
            # until l = r
            l += 1
            r -= 1

        return True