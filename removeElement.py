class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = len(nums) - 1
        while i != -1:
            if nums[i] == val:
                del nums[i]
            i = i - 1
