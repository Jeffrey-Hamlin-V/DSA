from typing import List

from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res=defaultdict(list)        
        for w in strs:
            c=[0]*26
            for i in w:
                c[ord(i)-ord("a")]+=1
            res[tuple(c)].append(w)
        return list(res.values())