class Solution:
    def makeGood(self, s: str) -> str:
        stack = []
        
        for let in s:
            if stack and abs(ord(stack[-1]) - ord(let)) == 32:
                stack.pop()
            else:
                stack.append(let)
                
        return ''.join(stack)