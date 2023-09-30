class Solution:
    def isValid(self, s: str) -> bool:
        opening_parens = set('({[')

        matches = {
            ')': '(',
            '}': '{',
            ']': '['
        }
        
        stack = []

        for char in s:
            if char in opening_parens:
                stack.append(char)
            else:
                if stack and stack[-1] == matches[char]:
                    stack.pop()
                else:
                    return False

        return stack == []