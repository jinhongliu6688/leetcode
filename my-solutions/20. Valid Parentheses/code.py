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
        # initilize an empty deque to serve as a stack
        stack = collections.deque()
        
        # iterate the letters in string s
        for l in s:
            # if the stack is empty, append the letter to the stack 
            if not stack:
                stack.append(l)
            # if the current letter is (, check if the top element in the stack is ). If it is, pop the top element
            elif l == ")" and stack[-1] == "(":
                stack.pop()
            # if the current letter is [, check if the top element in the stack is ]. If it is, pop the top element
            elif l == "]" and stack[-1] == "[":
                stack.pop()
            # if the current letter is {, check if the top element in the stack is }. If it is, pop the top element
            elif l == "}" and stack[-1] == "{":
                stack.pop()
            # if the above conditions do not met, add the letter to the stack
            # in other words, we add ( or [ or { in this step
            else:
                stack.append(l)
        
        # after the iteration, check if the stack is empty and return the result
        return len(stack) == 0
            else:
                stack.append(l)
        return len(stack) == 0
