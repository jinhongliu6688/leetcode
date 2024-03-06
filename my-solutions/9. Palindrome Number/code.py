# time: O(log n)
# space: O(log n)

class Solution:
    def isPalindrome(self, x: int) -> bool:
        # return the result of comparing the reverse string representation of x and the string representation of x
        return str(x)[::-1] == str(x)
