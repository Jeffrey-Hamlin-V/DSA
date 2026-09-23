class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        characters = set()
        left = 0
        longest = 0

        for right, character in enumerate(s):
            while character in characters:
                characters.remove(s[left])
                left += 1

            characters.add(character)
            longest = max(longest, right - left + 1)

        return longest
