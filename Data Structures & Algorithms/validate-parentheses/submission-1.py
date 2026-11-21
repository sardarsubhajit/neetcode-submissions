class Solution:
    def isValid(self, s: str) -> bool:
        if not s:
            return False
        
        pair = {
            ')': '(',
            '}': '{',
            ']': '['
        }
        stack = []
        for item in s:
            if item in pair:
                if stack and pair[item] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(item)
        
        if stack:
            return False
        else:
            return True