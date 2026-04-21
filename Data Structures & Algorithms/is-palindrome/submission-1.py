class Solution:
    def isPalindrome(self, s: str) -> bool:
        newStr = ''
        for c in s:
            if c.isalnum():
                newStr += c.lower()
        return newStr == newStr[::-1] 
        # reverse of the string
        # slicing syntax but skips start and stop, 
        # tells python to move through sequence backwards, one at a time