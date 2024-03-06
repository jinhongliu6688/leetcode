# method 1
class Solution:
    def romanToInt(self, s: str) -> int:
        num = 0

        sym_val = {
            "I" : 1,
            "V" : 5,
            "X" : 10,
            "L" : 50,
            "C" : 100,
            "D" : 500,
            "M" : 1000,
        }

        if "IV" in s:
            s = s.replace("IV", "")
            num += 4
        if "IX" in s:
            s = s.replace("IX", "")
            num += 9
        if "XL" in s:
            s = s.replace("XL", "")
            num += 40
        if "XC" in s:
            s = s.replace("XC", "")
            num += 90
        if "CD" in s:
            s = s.replace("CD", "")
            num += 400
        if "CM" in s:
            s = s.replace("CM", "")
            num += 900

        for l in s:
            num += sym_val[l]

        return num

# method 2
class Solution:
    def romanToInt(self, s: str) -> int:
        num = 0

        sym_val = {
            "I" : 1,
            "V" : 5,
            "X" : 10,
            "L" : 50,
            "C" : 100,
            "D" : 500,
            "M" : 1000,
        }

        for i, letter in enumerate(s):
            if i < len(s) - 1 and sym_val[s[i]] < sym_val[s[i + 1]] and i < len(s) - 1:
                    num -= sym_val[letter]
            else:
                num += sym_val[letter]

        return num
