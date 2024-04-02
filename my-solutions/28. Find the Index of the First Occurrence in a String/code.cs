public class Solution {
    public int StrStr(string haystack, string needle) {
        int i = 0;
        int needleLength = needle.Length;

        while (i + needleLength <= haystack.Length)
        {
            if (haystack.Substring(i, needleLength) == needle)
            {
                return i;
            }
            
            i += 1;
        }
      
        return -1;
    }
}
