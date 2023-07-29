# This is one application of how stack can be helful to solve a large mathematical problem
# Here we will take an empty stack and will fill it by values according to parenthesis open-close
# We will consider some signs and do the mathematical operations according to them

# Example : 5 * (4 + (18-2)/4) - 10

class Solve_Maths:
    def __init__(self, string) -> None:
        self.string = string
    
    def __operations(self, num1, operand, num2):
        if operand == "+":
            result = num1 + num2
        elif operand == "-":
            result = num1 - num2
        elif operand == "*":
            result = num1 * num2
        else:
            result = num1 / num2
        return result

    def push_pop_solve(self):
        stack = []
        i = 0
        
        return stack[0]

Obj = Solve_Maths("5*(4+(18-2)/4)-10")
print(f"The result is: {Obj.push_pop_solve()}")


    
