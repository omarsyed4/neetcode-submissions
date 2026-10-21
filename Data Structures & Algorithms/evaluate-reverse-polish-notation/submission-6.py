class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        stack = []
        

        for t in tokens:
            if t == '+':
                op1 = stack.pop()
                op2 = stack.pop()
                curr = int(op1) + int(op2)
                stack.append(curr)
            elif t == '-':
                op1 = stack.pop()
                op2 = stack.pop()
                curr = int(op2) - int(op1)
                stack.append(curr)
            elif t == '*':
                op1 = stack.pop()
                op2 = stack.pop()
                curr = int(op1) * int(op2)
                stack.append(curr)
            elif t == '/':
                op1 = stack.pop()
                op2 = stack.pop()
                curr = int(op2) / int(op1)
                stack.append(curr)
            else:
                stack.append(t)


            
        return int(stack.pop())