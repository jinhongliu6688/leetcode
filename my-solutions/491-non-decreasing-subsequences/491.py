class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        result = []
        length = len(nums)

        def dfs(begin, path):
            if len(path) >= 2:
                result.append(path)
            
            if begin == length:
                return

            seen = {}
            for index in range(begin, length):
                if seen.get(nums[index]) == 1:
                    continue
                if len(path) > 0 and nums[index] < path[-1]:
                    continue
                seen[nums[index]] = 1
                dfs(index + 1, path + [nums[index]])

        dfs(0, [])

        return result
