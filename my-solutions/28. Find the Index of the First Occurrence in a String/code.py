class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # initialize index i
        i = 0
        # set index j to be the length of needle
        j = len(needle)

        # while j is less then or equal to the length of haystack
        while j <= len(haystack):

            # the current substring of haystack is equal to needle, return index i
            if haystack[i:j] == needle:
                return i
            
            # if the above condition is not met, increase index i and index j
            i += 1
            j += 1
        
        # return -1 when needle is not part of haystack 
        return -1
