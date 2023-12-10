class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        def to_abc_word(word, order):
            return "".join(["abcdefghijklmnopqrstuvwxyz"[order.index(i)] for i in word])

        return words == sorted(words, key=lambda x: to_abc_word(x, order))
