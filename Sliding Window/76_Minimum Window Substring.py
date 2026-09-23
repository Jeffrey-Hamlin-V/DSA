from collections import Counter, defaultdict


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s:
            return ""

        needed = Counter(t)
        window = defaultdict(int)
        required = len(needed)
        formed = 0
        left = 0
        smallest = (float("inf"), 0, 0)

        for right, character in enumerate(s):
            window[character] += 1

            if character in needed and window[character] == needed[character]:
                formed += 1

            while formed == required:
                if right - left + 1 < smallest[0]:
                    smallest = (right - left + 1, left, right)

                left_character = s[left]
                window[left_character] -= 1
                if left_character in needed and window[left_character] < needed[left_character]:
                    formed -= 1
                left += 1

        length, start, end = smallest
        return "" if length == float("inf") else s[start:end + 1]
