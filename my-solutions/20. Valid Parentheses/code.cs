public class Solution {
    public bool IsValid(string s) {
        Stack myStack = new Stack();

        foreach(char c in s)
        {
            if (myStack.Count == 0)
            {
                myStack.Push(c);
            }
            else if (c == ')' && (char)myStack.Peek() == '(')
            {
                myStack.Pop();
            }
            else if (c == ']' && (char)myStack.Peek() == '[')
            {
                myStack.Pop();
            }
            else if (c == '}' && (char)myStack.Peek() == '{')
            {
                myStack.Pop();
            }
            else
            {
                myStack.Push(c);
            }
        }

        return myStack.Count == 0;
    }
}
