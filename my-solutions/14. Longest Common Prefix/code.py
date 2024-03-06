class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        # saved the first word for later comparison
        first_word = strs[0]

        # initilize result
        result = ""

        # iterate the letters in the first word
        for i, letter in enumerate(first_word):
            # iterate the words in strs
            for word in strs:
                # if the index is out of bound of the current word
                # or if the letters do not match
                # return the current result
                if i > len(word) - 1 or word[i] != first_word[i]:
                    return result
            # all the words in strs have the current letter, add the letter to result
            result += letter

        # return the result
        return result
