class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Maps a number to the length of the consecutive sequence it belongs to.
        # Only boundary values (left and right endpoints) are kept accurate.
        mp = defaultdict(int)
        res = 0

        for num in nums:
            # Skip if already part of a sequence (was previously set as a boundary)
            if not mp[num]:
                # Calculate new sequence length by merging:
                # - the sequence ending at (num - 1), length = mp[num - 1]
                # - num itself (+1)
                # - the sequence starting at (num + 1), length = mp[num + 1]
                mp[num] = mp[num - 1] + mp[num + 1] + 1

                # Update the LEFT endpoint of the merged sequence to the new total length.
                # (num - mp[num - 1]) walks back to the start of the left sequence.
                mp[num - mp[num - 1]] = mp[num]

                # Update the RIGHT endpoint of the merged sequence to the new total length.
                # (num + mp[num + 1]) walks forward to the end of the right sequence.
                mp[num + mp[num + 1]] = mp[num]

                res = max(res, mp[num])

        return res