class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        letters_list = list(pattern)
        words_list = s.split()

        if len(letters_list) != len(words_list):
            return False

        dict_1 = {}

        for i, word in enumerate(words_list):
            if letters_list[i] in dict_1.keys():
                if dict_1[letters_list[i]] != word:
                    return False
            elif word in dict_1.values():
                return False
            else:
                dict_1[letters_list[i]] = word
        
        return True
