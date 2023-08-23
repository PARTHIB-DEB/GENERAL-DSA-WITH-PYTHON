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
        self.operandlist = ["^","*","/","+","-"]
        self.infix = list(infix)
        self.stack = []
        self.postfix = ""

    def precedence(self, item) -> int: # Precedence Checker Function
        if item == "^":
            return 3
        elif item == "*" or item == "/":
            return 2
        elif item == "+" or item == "-":
            return 1
        else:
            return 0      

    def conversion(self):
        self.stack.insert(0,"(") #It says that now we can operate the equation from start
        self.infix.append(")") # It says that Our operations has ended
        i = 0
        while(i<len(self.infix)):
            item=self.infix[i]
            if item=="(":
                self.stack.append(item)
                
            elif str(item).isalnum():
                self.postfix+=str(item)
                
            elif item in self.operandlist:
                x=self.stack.pop()
                while x in self.operandlist and self.precedence(x)>=self.precedence(item): # Checking Precedence of stack(top) and new-elem
                    self.postfix+=x
                    x=self.stack.pop()
                self.stack.append(x)
                self.stack.append(item)
                
            elif item==")": # If we see the ending bracket , then repeatedly just put stack elems in postfix expr
                x=self.stack.pop()
                while x != "(":
                    self.postfix+=x
                    x=self.stack.pop()
            i+=1
        return self.postfix

expression = "A+(B-(C/D)*E)-F"
converter = InfixToPostfix(expression)
postfix_result = converter.conversion()
print("\n\t\t%s IN POSTFIX : %s\n" %(expression,postfix_result))
