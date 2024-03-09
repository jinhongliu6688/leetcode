class Solution(object):
    def isValid(self, s):
        while "()" in s or "{}" in s or '[]' in s:
            s = s.replace("()", "").replace('{}', "").replace('[]', "")
        return s == ''


# time: O(n^2)
# space: O(n)
class Solution:
    def isValid(self, s: str) -> bool:
        previous_length = len(s)
        while len(s) > 0:
            if "()" in s:
                s = s.replace("()", "")
            if "[]" in s:
                s = s.replace("[]", "")
            if "{}" in s:
                s = s.replace("{}", "")
            if len(s) == previous_length:
                return False
            previous_length = len(s)
        return True

# time: O(n)
# space: O(n)
class Solution:
    def isValid(self, s: str) -> bool:
        stack = collections.deque()
        for l in s:
            if not stack:
                stack.append(l)
            elif l == ")" and stack[-1] == "(":
                stack.pop()
            elif l == "]" and stack[-1] == "[":
                stack.pop()
            elif l == "}" and stack[-1] == "{":
                stack.pop()
            else:
                stack.append(l)
        return len(stack) == 0
