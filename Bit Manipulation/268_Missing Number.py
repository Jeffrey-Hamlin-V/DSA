class Solution:
 def missingNumber(self,nums):
  result=len(nums)
  for i,n in enumerate(nums):result^=i^n
  return result
