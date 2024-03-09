public class Solution {
    public string LongestCommonPrefix(string[] strs) {
        string first_word = strs[0];

        string result = "";

        for (int i = 0; i <= first_word.Length - 1; i++)
        {
            foreach (string str in strs)
            {
                if (i > str.Length - 1 || str[i] != first_word[i])
                {
                    return result;
                }
            }
            result += first_word[i];
        }
        return result;
    }
}
