class Solution:
    def isValid(self, s: str) -> bool:

        char_stack = []

        for char in s:
            if char == "(" or char == "[" or char == "{":
                char_stack.append(char)
            elif char == ")":
                if not char_stack or char_stack.pop() != "(":
                    return False
            elif char == "]":
                if not char_stack or char_stack.pop() != "[":
                    return False
            elif char == "}":
                if not char_stack or char_stack.pop() != "{":
                    return False
        return not char_stack

            
        