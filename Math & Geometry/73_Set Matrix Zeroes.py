class Solution:
 def setZeroes(self,matrix):
  rows={r for r,row in enumerate(matrix) for c,n in enumerate(row) if n==0};cols={c for r,row in enumerate(matrix) for c,n in enumerate(row) if n==0}
  for r in range(len(matrix)):
   for c in range(len(matrix[0])):
    if r in rows or c in cols:matrix[r][c]=0
