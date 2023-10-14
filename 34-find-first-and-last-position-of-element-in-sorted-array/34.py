class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        ans_1 = -1
        ans_2 = -1

        l = 0
        r = len(nums) - 1

        while l <= r:
            m = (l + r) // 2
            if nums[m] == target:
                ans_1 = m
                r = m - 1
            elif nums[m] < target:
                l = m + 1
            elif nums[m] > target:
                r = m - 1
        l = 0
        r = len(nums) - 1

        while l <= r:
            m = (l + r) // 2
            if nums[m] == target:
                ans_2 = m
                l = m + 1
            elif nums[m] < target:
                l = m + 1
            elif nums[m] > target:
                r = m - 1

        return [ans_1, ans_2]
