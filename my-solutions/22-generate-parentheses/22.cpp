class Solution {
public:
    vector<string> result;
    vector<string> generateParenthesis(int n) {
        dfs("", n, n);
        return result;
    }

    void dfs(string cur_str, int left_count, int right_count) {
        if (left_count == 0 and right_count == 0) {
            result.push_back(cur_str);
            return;
        }

        if (left_count > right_count) {
            return;
        }

        if (left_count > 0) {
            dfs(cur_str + "(", left_count - 1, right_count);
        }

        if (right_count > 0) {
            dfs(cur_str + ")", left_count, right_count - 1);
        }

    }


};
