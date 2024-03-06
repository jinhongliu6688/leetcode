# Time complexity: O(n)
# Space complexity: O(n)

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Create an empty dictionary to store the numbers and their indices
        dict_1 = {}

        # Iterate through the list of numbers along with their indices
        for i, num in enumerate(nums):
            # if the dictionary is empty, add the current number to the dictionary as key and set its index as value
            if not dict_1:
                dict_1[num] = i
            # if the component of current number is in the dictionary, return the index of the current number and the index of the component
            elif target - num in dict_1:
                return [i, dict_1[target - num]]
            # if the current number does not exist in the dictionary, add the current number to the dictionary along with its index
            else:
                dict_1[num] = i
