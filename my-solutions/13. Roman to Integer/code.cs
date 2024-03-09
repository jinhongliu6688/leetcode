public class Solution {
    public int RomanToInt(string s) {
        int num = 0;

        s = s.Replace("IV", "a");
        s = s.Replace("IX", "b");
        s = s.Replace("XL", "c");
        s = s.Replace("XC", "d");
        s = s.Replace("CD", "e");
        s = s.Replace("CM", "f");

        Dictionary<char, int> dict_1 = new Dictionary<char, int>();
        dict_1.Add('I', 1);
        dict_1.Add('V', 5);
        dict_1.Add('X', 10);
        dict_1.Add('L', 50);
        dict_1.Add('C', 100);
        dict_1.Add('D', 500);
        dict_1.Add('M', 1000);
        dict_1.Add('a', 4);
        dict_1.Add('b', 9);
        dict_1.Add('c', 40);
        dict_1.Add('d', 90);
        dict_1.Add('e', 400);
        dict_1.Add('f', 900);

        foreach(char letter in s)
        {
            num += dict_1[letter];
        }

        return num;
    }
}
