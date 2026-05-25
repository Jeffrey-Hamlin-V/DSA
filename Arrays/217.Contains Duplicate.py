class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        og=set(nums)
        if(len(og)==len(nums)):
            return False
        return True