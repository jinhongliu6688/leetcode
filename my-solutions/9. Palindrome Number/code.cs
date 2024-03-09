public class Solution {
    public bool IsPalindrome(int x) {

        // initialize a string to store the string format of x
        string x_string = x.ToString();

        // convert the string to a char array
        char[] x_string_array = x_string.ToCharArray();

        // reverse the array
        Array.Reverse(x_string_array);

        // convert the char array back to string
        string x_string_reversed = new string(x_string_array);
        
        // compare the string and its reversed version and return the result
        return x_string == x_string_reversed;
    }
}
