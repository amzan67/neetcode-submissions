from statistics import mode
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
     num = []

     while len(num) < k:
            common = mode(nums)
            num.append(common)
            # Remove ALL instances of the mode element from nums
            nums = [x for x in nums if x != common]
            
     return num