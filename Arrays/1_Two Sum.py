class Solution(object):
    def twoSum(self, nums, target):
        d={}
        for i,x in enumerate(nums):
            t=target-x
            if(t in d):
                return [i,d[t]]
            d[x]=i