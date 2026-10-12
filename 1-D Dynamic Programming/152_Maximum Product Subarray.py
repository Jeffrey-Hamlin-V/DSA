class Solution:
 def maxProduct(self,nums):
  best=high=low=nums[0]
  for n in nums[1:]: high,low=max(n,high*n,low*n),min(n,high*n,low*n);best=max(best,high)
  return best
