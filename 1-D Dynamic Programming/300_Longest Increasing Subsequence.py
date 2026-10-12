from bisect import bisect_left
class Solution:
 def lengthOfLIS(self,nums):
  tails=[]
  for n in nums:
   i=bisect_left(tails,n)
   if i==len(tails):tails.append(n)
   else:tails[i]=n
  return len(tails)
