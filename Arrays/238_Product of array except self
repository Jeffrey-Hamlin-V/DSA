class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        arr=[1]*len(nums)
        cur=1
        for i,x in enumerate(nums):
            arr[i]=cur
            cur*=x
        cur=1
        for i in range(len(nums)-1,-1,-1):
            arr[i]*=cur
            cur*=nums[i]
        return arr
