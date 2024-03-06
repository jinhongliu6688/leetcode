# time: O(n)
# space: O(1)

class Solution:
    def romanToInt(self, s: str) -> int:

        # Initialize the answer for return
        num = 0

        # Create a dicitonary to store the symbols and corresponding values.
        sym_val = {
            "I" : 1,
            "V" : 5,
            "X" : 10,
            "L" : 50,
            "C" : 100,
            "D" : 500,
            "M" : 1000,
        }

        # Special cases where a symbol with smaller value precede a symbol with larger value
        # When there is a special case in s, replace the speical case with empty string and add the corresponding value to the result
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

        # Deal with normal cases
        # Iterate the letters of string s and add the corresponding values to the result
        for l in s:
            num += sym_val[l]

        return num

# time: O(n)
# space: O(1)

class Solution:
    def romanToInt(self, s: str) -> int:

        # Initialize the answer for return
        num = 0

        # Replace the special cases with corresponding single letter placeholders
        s = s.replace("IV", "a")
        s = s.replace("IX", "b")
        s = s.replace("XL", "c")
        s = s.replace("XC", "d")
        s = s.replace("CD", "e")
        s = s.replace("CM", "f")

        # Create a dicitonary to store the symbols and corresponding values.
        sym_val = {
            "I" : 1,
            "V" : 5,
            "X" : 10,
            "L" : 50,
            "C" : 100,
            "D" : 500,
            "M" : 1000,
            "a" : 4,
            "b" : 9,
            "c" : 40,
            "d" : 90,
            "e" : 400,
            "f" : 900,
        }

        # Iterate the letters of string s and add the corresponding values to the result
        for l in s:
            num += sym_val[l]

        return num

# time: O(n)
# space: O(1), fixed size of the dictionary

class Solution:
    def romanToInt(self, s: str) -> int:

        # Initialize the answer for return
        num = 0

        # Create a dicitonary to store the symbols and corresponding values.
        sym_val = {
            "I" : 1,
            "V" : 5,
            "X" : 10,
            "L" : 50,
            "C" : 100,
            "D" : 500,
            "M" : 1000,
        }

        # Iterate the letters in string s. If the current index is not the last index and the current symbol's value is less than next symbol's value, subtract the current value from num. Otherwise, add the current symbol's value to num.
        for i, letter in enumerate(s):
            if i < len(s) - 1 and sym_val[s[i]] < sym_val[s[i + 1]] and i < len(s) - 1:
                    num -= sym_val[letter]
            else:
                num += sym_val[letter]

        # Return num as the result
        return num
