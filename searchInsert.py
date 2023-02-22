class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        for i in range(len(nums)):
            if nums[i] == target:
                return i
        if target > nums[len(nums) - 1]:
            return len(nums)
        if target < nums[0]:
            return 0
        for i in range(len(nums)-1):
            if nums[i] < target and nums[i+1] > target:
                print(nums[i])
                i = i + 1
                break
        return i
