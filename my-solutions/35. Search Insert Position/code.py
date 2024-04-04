# time: O(n)
# space: O(1)

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:

        # if the target is greater than the last element in nums
        # the insert position is the last position
        if target > nums[-1]:
            return len(nums)

        # if the target is less than the first element in nums
        # the insert position is the first position
        elif target < nums[0]:
            return 0

        # iterate the number in nums
        for i, num in enumerate(nums):
            # if the number is the same as the target, return the current position
            if num == target:
                return i
            # if the current number is less than the target and the next number is larger than the target
            # return the next position
            elif num < target and nums[i+1] >= target:
                return i + 1
