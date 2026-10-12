class Solution:
 def insert(self,intervals,newInterval):
  result=[];i=0
  while i<len(intervals) and intervals[i][1]<newInterval[0]:result.append(intervals[i]);i+=1
  while i<len(intervals) and intervals[i][0]<=newInterval[1]:newInterval=[min(newInterval[0],intervals[i][0]),max(newInterval[1],intervals[i][1])];i+=1
  return result+[newInterval]+intervals[i:]
