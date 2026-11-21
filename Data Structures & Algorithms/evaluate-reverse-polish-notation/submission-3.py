class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token == '+' and len(stack) >= 2:
                y, x = stack.pop(), stack.pop()
                stack.append(x+y)
            elif token == '-' and len(stack) >= 2:
                y, x = stack.pop(), stack.pop()
                stack.append(x-y)
            elif token == '*' and len(stack) >= 2:
                y, x = stack.pop(), stack.pop()
                stack.append(x*y)
            elif token == '/' and len(stack) >= 2:
                y, x = stack.pop(), stack.pop()
                stack.append(int(x/y))
            else:
                stack.append(int(token))
        
        return stack[0] if stack else None