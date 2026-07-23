class Solution:
    def isValid(self, s: str) -> bool:
        bracket_match = {")": "(", "]": "[", "}": "{"}
        open_stack = []
        open_chars = "({["
        
        for char in s:
            if char in open_chars:
                open_stack.append(char)
            else:
                if not open_stack:
                    return False
                top_char = open_stack.pop()
                if top_char != bracket_match[char]:
                    return False
        
        return not open_stack