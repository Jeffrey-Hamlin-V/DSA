from collections import defaultdict


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counts = defaultdict(int)
        left = 0
        most_frequent = 0

        for right, character in enumerate(s):
            counts[character] += 1
            most_frequent = max(most_frequent, counts[character])

            while right - left + 1 - most_frequent > k:
                counts[s[left]] -= 1
                left += 1

        return right - left + 1 if s else 0
