from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        combinations = []

        def backtrack(start: int, remaining: int, current: List[int]) -> None:
            if remaining == 0:
                combinations.append(current[:])
                return

            for index in range(start, len(candidates)):
                candidate = candidates[index]
                if candidate > remaining:
                    continue
                current.append(candidate)
                backtrack(index, remaining - candidate, current)
                current.pop()

        backtrack(0, target, [])
        return combinations
