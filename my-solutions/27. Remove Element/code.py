# time: O(n)
# space: O(1)

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:

        # initialize index i pointing to numbers equal to val
        i = 0

        # initialize index j pointing to numbers not equal to val
        j = 0

        length = len(nums)
        
        # while i and j are both within bound of nums
        while i < length and j < length:

            # i is always point to num with value val
            while i < length and nums[i] != val:
                i += 1

            # j is always point to num not with value val
            while j < length and nums[j] == val:
                j += 1
            
            # if i is less than j, switch the values
            if i < j and i < length and j < length:
                nums[i], nums[j] = nums[j], nums[i]
            # else move j forward
            else:
                j += 1

        # i is the first num of value val 
        return i
