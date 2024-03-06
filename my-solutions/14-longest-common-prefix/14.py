class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        first_word = strs[0]

        i = 0
        answer = ""

        for letter in first_word:
            for word in strs:
                if i > len(word) - 1 or word[i] != letter:
                    return answer
            answer += letter
            i += 1
        
        return answer
