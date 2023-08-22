# It's an application of stack which means we have to do the conversion using stack
'''
Functions --> isdigit , isoperator , push , pop (Some of here are built-in) , precedence
Rules:
    1) Create a stack (list) : Purpose of stack is to fill operands in it after putting first "(" in it and pop if found any ")" in the expr
    2) Create a postfix (string or list) : If expr(item) is not operand , straight fill it in postfix , if it is , follow the below rules
    3) Pushing/Popping in stack Rules :
        #### If precedence(expr(item))>=precedence(stack(top)) pop stack(top) and insert in postfix
        #### If ")" is found in expr , repeateadly pop stack(top) untill ")" appears
        Otherwise
        #### Push in stack 
'''
class InfixToPostfix:
    def __init__(self, infix) -> None:
        self.operandlist = "^*/+-"
        self.infix = infix
        self.stack = []
        self.postfix = ""

    def precedence(self, item) -> int:
        if item == '^':
            return 3
        elif item == "*" or item == "/":
            return 2
        elif item == "+" or item == "-":
            return 1
        else:
            return 0

    def conversion(self):
        self.stack.append("(")
        self.infix += ")"
        i = 0
        infix_elm = self.infix[i]
        while (i<=len(self.infix)-1):
            if infix_elm == "(":
                self.stack.append(self.infix[i])
                
            elif infix_elm not in self.operandlist:
                self.postfix += self.infix[i]
                
            elif infix_elm in self.operandlist:
                item = self.stack.pop()
                while (item in self.operandlist and self.precedence(item) >= self.precedence(infix_elm)):
                    self.postfix += item
                    item = self.stack.pop()
                self.stack.append(item)
                self.stack.append(infix_elm)
                
            elif infix_elm == ")":
                item = self.stack.pop()
                while (item != "("):
                    self.postfix += item
                    item = self.stack.pop()
                    
            else:
                print("\n\t\tINVALID EXPRESSION")
                break
            infix_elm = self.infix[i]
            i+=1
        while(len(self.stack)>0):
            item = self.stack.pop()
            self.postfix+=item
        return self.postfix

expression = "A+(B-(C/D)*E)-F"
converter = InfixToPostfix(expression)
postfix_result = converter.conversion()
print(postfix_result)
