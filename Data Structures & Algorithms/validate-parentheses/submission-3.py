class Solution:
    def isValid(self, s: str) -> bool:

        open_brackets = '({['
        closed_brackets = ')}]'

        stack = []

        for i in range(len(s)):

            if s[i] in open_brackets:
                stack.append(s[i])
                continue

            else:
                if not stack:
                    return False
                elif s[i] == ')' and stack[-1] == '(':
                    stack.pop()
                elif s[i] == ')' and stack[-1] != '(':
                    return False
                elif s[i] == '}' and stack[-1] == '{':
                    stack.pop()
                elif s[i] == '}' and stack[-1] != '{':
                    return False
                elif s[i] == ']' and stack[-1] == '[':
                    stack.pop()
                elif s[i] == ']' and stack[-1] != '[':
                    return False
        
        return len(stack) == 0

        