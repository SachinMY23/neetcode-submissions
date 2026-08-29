# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:
        flist= []
        if (len(pairs)<1):
            return flist
        flist.append(pairs[:])
        for i in range(1, len(pairs)):
            j=i
            went_index= j
            while(j>0 and pairs[j].key<pairs[j-1].key):
                item= pairs[j]
                pairs[j]= pairs[j-1]
                pairs[j-1] =item
                j -= 1
                went_index -= 1
            flist.append(pairs[:])
        return flist
            
            

            

        