# This is one application of how stack can be helful to solve a large mathematical problem
# Here we will take an empty stack and will fill it by values according to parenthesis open-close
# We will consider some signs and do the mathematical operations according to them

# Example : 5 * (4 + (18-2)/4) - 10
class Solve_Maths:
    def __init__(self, string) -> None:
        self.string = string
    
    @classmethod
    def operations(self, num1, operand, num2):
        if operand == "+":
            return (int(num1) + int(num2))
        elif operand == "-":
            return (int(num1) - int(num2))
        elif operand == "*":
            return (int(num1) * int(num2))
        else:
            return (int(num1) / int(num2))
    
    stack=[]
    flag=1
    def push_pop_solve(self):
        for i in self.string:
            if i == ')':
                print(self.stack)
                num2,operand,num1 = self.stack.pop(),self.stack.pop(),self.stack.pop()
                result=self.operations(num1=num1,operand=operand,num2=num2)
                self.stack.append(result)
                self.flag=0
            else:
                if i != '(':
                    self.stack.append(i)
        # return self.stack


Obj=Solve_Maths("5*(4+(18-2)/4)-10")
print(f"The result is : {Obj.push_pop_solve()}")


    
