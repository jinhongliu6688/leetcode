# Time complexity: O(n)
# Space complexity: O(n)

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict_1 = {}

        for i, num in enumerate(nums):
            if not dict_1:
                dict_1[num] = i
            elif target - num in dict_1:
                return [i, dict_1[target - num]]
            else:
                dict_1[num] = i
