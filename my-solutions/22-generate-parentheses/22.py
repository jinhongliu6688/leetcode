class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []

        def dfs(cur_str, left_count, right_count):
            if left_count == 0 and right_count == 0:
                result.append(cur_str)
                return
            
            if left_count > right_count:
                return

            if left_count > 0:
                dfs(cur_str + "(", left_count - 1, right_count)

            if right_count > 0:
                dfs(cur_str + ")", left_count, right_count - 1)

        dfs("", n, n)
        return result
