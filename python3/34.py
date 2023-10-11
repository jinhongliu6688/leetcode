class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        i = 0
        j = len(nums) - 1
        m = -1
        bool = False

        while i <= j:
            m = (i + j) // 2
            if nums[m] == target:
                bool = True
                break
            elif nums[m] < target:
                i = m + 1
            elif nums[m] > target:
                j = m - 1
        
        if bool == False: return [-1, -1]

        r1 = m
        r2 = m

        i1 = 0
        j1 = m

        while i1 <= j1:
            m1 = (i1 + j1) // 2
            if nums[m1] == target:
                r1 = m1
                j1 = m1 - 1
            elif nums[m1] < target:
                i1 = m1 + 1
            elif nums[m1] > target:
                j1 = m1 - 1

        i2 = m
        j2 = len(nums) - 1

        while i2 <= j2:
            m2 = (i2 + j2) // 2
            if nums[m2] == target:
                r2 = m2
                i2 = m2 + 1
            elif nums[m2] < target:
                i2 = m2 + 1
            elif nums[m2] > target:
                j2 = m2 - 1

        return [r1, r2]
