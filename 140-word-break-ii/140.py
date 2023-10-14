class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        result = []

        def dfs(path, cur_str):

            if len(cur_str) == 0:
                result.append(" ".join(path))
                return
            
            for word in wordDict:
                if cur_str.startswith(word):
                    dfs(path + [word], cur_str[len(word):])

        dfs([], s)

        return result
