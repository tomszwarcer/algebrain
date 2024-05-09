from sympy import *

#Solves linear equations


class Side:
    def __init__(self, content):
        self.content = content

        #separate side into blocks:
        self.blocks = content.split(" + ")

class Equation:
    def __init__(self, content):
        #separate eqn into sides.
        #Create Side objects
        self.content = content
        self.lhs = Side(content.split(" = ")[0])
        self.rhs = Side(content.split(" = ")[1])   

    def update_content(self):
        # updates the written form of equation (for use with SymPy)
        self.content = self.lhs.content + " = " + self.rhs.content

    def flip_sides(self):
        # function to flip sides, e.g. to put subject on LHS

        temp = self.lhs
        self.lhs = self.rhs
        self.rhs = temp

        #update equation content:
        self.update_content()

def main():
    equation = Equation("3 + 5y = 2x")
    subject = "x"

    #collect like terms:
    #TODO: code for this. for now assume they have been collected.

    #check if sides should be flipped if subject is on rhs
    for block in equation.rhs.blocks:
        if subject in block:
            equation.flip_sides()

    print(equation.lhs.blocks)
    print(equation.rhs.blocks)

main()
