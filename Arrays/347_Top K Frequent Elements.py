from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c=defaultdict(int)
        for i in nums:
            c[i]+=1
        print(c)
        bucket=[[]for _ in range (len(nums)+1)]
        for ele,count in c.items():
            bucket[count].append(ele) 
        result=[]
        for count in range(len(bucket)-1,0,-1):
            result.extend(bucket[count])
            if(len(result)>=k):
                return result[:k]

