class Solution:
    def isValid(self, s: str) -> bool:
        matches = {
            '(': ')',
            '{': '}',
            '[': ']'
        }
        
        stack = []

        for char in s:
            if char in matches:
                stack.append(char)
            else:
                if stack and matches[stack[-1]] == char:
                    stack.pop()
                else:
                    return False

        return stack == []