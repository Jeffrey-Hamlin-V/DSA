class Solution:
 def coinChange(self,coins,amount):
  dp=[amount+1]*(amount+1);dp[0]=0
  for total in range(1,amount+1): dp[total]=min([dp[total-coin]+1 for coin in coins if coin<=total] or [amount+1])
  return dp[amount] if dp[amount]<=amount else -1
