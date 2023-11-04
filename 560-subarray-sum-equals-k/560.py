class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        map = {}
        sum_val = 0
        count = 0
        
        for num in nums:
            sum_val += num
            if sum_val == k:
                count += 1
            if sum_val - k in map:
                count += map[sum_val - k]
            if sum_val in map:
                map[sum_val] += 1
            else:
                map[sum_val] = 1
        
        return count
