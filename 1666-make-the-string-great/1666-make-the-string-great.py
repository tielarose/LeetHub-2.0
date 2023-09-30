class Solution:
    def makeGood(self, s: str) -> str:
        def inverse_letter(letter):
            return letter.lower() if letter.isupper() else letter.upper()
        
        stack = []
        
        for let in s:
            
            if stack and stack[-1] == inverse_letter(let):
                stack.pop()
            else:
                stack.append(let)
                
        return ''.join(stack)