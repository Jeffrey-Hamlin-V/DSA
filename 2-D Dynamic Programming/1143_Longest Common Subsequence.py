class Solution:
 def longestCommonSubsequence(self,text1,text2):
  dp=[0]*(len(text2)+1)
  for a in text1:
   previous=0
   for j,b in enumerate(text2,1): previous,dp[j]=dp[j],max(dp[j],dp[j-1],previous+1 if a==b else 0)
  return dp[-1]
