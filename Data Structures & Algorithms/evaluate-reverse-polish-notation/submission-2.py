class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = {"+", "-", "*", "/"}
        stack = []
        result = 0
        for token in tokens:
            if token == "+":
                a = stack.pop()
                b = stack.pop()
                stack.append(a+b)
                print(f"+ {stack}")
            elif token == "-":
                a = stack.pop()
                b = stack.pop()
                stack.append(b-a)
                print(f"- {stack}")
            elif token == "/":
                a = stack.pop()
                b = stack.pop()
                stack.append(int(b/a))
                print(f"/ {stack}")
            elif token == "*":
                a = stack.pop()
                b = stack.pop()
                stack.append(a*b)
                print(f"* {stack}")
            else:
                stack.append(int(token))

        
        return stack.pop()