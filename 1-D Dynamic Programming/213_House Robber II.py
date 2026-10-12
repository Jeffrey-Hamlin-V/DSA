class Solution:
 def rob(self,nums):
  def run(a):
   x=y=0
   for n in a: x,y=y,max(y,x+n)
   return y
  return nums[0] if len(nums)==1 else max(run(nums[1:]),run(nums[:-1]))
