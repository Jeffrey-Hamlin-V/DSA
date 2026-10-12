class Solution:
 def eraseOverlapIntervals(self,intervals):
  end=float('-inf');removed=0
  for start,finish in sorted(intervals,key=lambda x:x[1]):
   if start<end:removed+=1
   else:end=finish
  return removed
