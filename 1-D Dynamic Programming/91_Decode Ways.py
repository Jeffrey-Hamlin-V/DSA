class Solution:
 def numDecodings(self,s):
  if not s or s[0]=='0': return 0
  a=b=1
  for i in range(1,len(s)): a,b=b,(b if s[i]!='0' else 0)+(a if 10<=int(s[i-1:i+1])<=26 else 0)
  return b
