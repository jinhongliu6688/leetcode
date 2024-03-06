class Solution {
    public List<String> generateParenthesis(int n) {
        List<String> result = new ArrayList<String>();
        dfs("", n, n, result);
        return result;
    }

    public void dfs(String cur_str, int left_count, int right_count, List<String> result) {
        if (left_count == 0 && right_count == 0) {
            result.add(cur_str);
            return;
        }

        if (left_count > right_count) {
            return;
        }

        if (left_count > 0) {
            dfs(cur_str + "(", left_count - 1, right_count, result);
        }

        if (right_count > 0) {
            dfs(cur_str + ")", left_count, right_count - 1, result);
        }
    }
}
