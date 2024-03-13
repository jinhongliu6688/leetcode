# time: O(n)
# space: O(1)

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # initialize insert_index to 1
        insert_index = 1

        # iterate the number is nums and skip the first number
        for i in range(1, len(nums)):
            # if the current number is different to the last number, 
            # replace the number at the insertion index with the current number
            if nums[i] != nums[i-1]:
                nums[insert_index] = nums[i]
                # move the insertion index forward
                insert_index += 1
        
        # The final value of insert_index represents the length of the modified array
        return insert_index
