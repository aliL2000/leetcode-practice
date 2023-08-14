class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for str in tokens:
            if str == "+":
                stack.append(stack.pop()+stack.pop())
            elif str == "*":
                stack.append(stack.pop()*stack.pop())
            elif str == "-":
                a,b = stack.pop(),stack.pop()
                stack.append(b-a)
            elif str == "/":
                a,b = stack.pop(),stack.pop()
                stack.append(int(b/a))
            else:
                stack.append(int(str))
        return stack[0]