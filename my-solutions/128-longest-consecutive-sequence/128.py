# method 1
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        nums.sort()
        longest = 1
        length = 1
        for i, num in enumerate(nums):
            if i == 0:
                continue
            elif nums[i] == nums[i-1] + 1:
                length += 1
            elif nums[i] == nums[i-1]:
                continue
            else:
                longest = max(length, longest)
                length = 1
        
        return max(length, longest)


# method 2
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        nums = sorted(list(set(nums)))
        longest = 1
        length = 1
        for i, num in enumerate(nums):
            if i == 0:
                continue
            elif nums[i] == nums[i-1] + 1:
                length += 1
            else:
                longest = max(length, longest)
                length = 1
        
        return max(length, longest)
