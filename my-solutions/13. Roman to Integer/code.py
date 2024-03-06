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
