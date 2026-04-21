class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
            # every string becomes length#string
            # is a clear boundary, length ensures exact characters
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0 # pointer starts at 0

        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1 # moving pointer j forward until it finds '#'
            length = int(s[i:j])
            i = j + 1 # moving i to the character right after '#'
            j = i + length # moving j to the character right after the "string"
            res.append(s[i:j]) # append extracted string to results
            i = j # move i forward by length to continue the next decoding

        return res