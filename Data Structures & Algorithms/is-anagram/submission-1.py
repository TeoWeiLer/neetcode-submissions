class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        char_map1 = {}
        char_map2 = {}

        for c in s:
            if c not in char_map1:
                char_map1[c] = 1
            else:
                char_map1[c] += 1

        for c in t:
            if c not in char_map2:
                char_map2[c] = 1
            else:
                char_map2[c] += 1

        return char_map1 == char_map2
        