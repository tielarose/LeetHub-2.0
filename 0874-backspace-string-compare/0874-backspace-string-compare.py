class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def remove_hash(input_str):
            stack = []

            for char in input_str:
                if char != '#':
                    stack.append(char)
                elif stack:
                    stack.pop()

            return ''.join(stack)

        return remove_hash(s) == remove_hash(t)