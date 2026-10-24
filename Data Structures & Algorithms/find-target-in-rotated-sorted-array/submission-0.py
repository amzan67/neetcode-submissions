class Solution:
    def search(self, nums: List[int], target: int) -> int:
        for i in nums:
            if target in nums:
                index = nums.index(target)
                return index
            else:
                return -1