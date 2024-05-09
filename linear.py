from sympy import *

#Solves linear equations
#in its current form, isolates whatever has an 'x' in it. Can't collect terms or divide.
#also can't deal with negative coefficients
#TODO: add collecting like terms functionality
#TODO: implement division
#TODO: implement support for negative coeffs
#TODO: give some indication when original equation has been flipped

class Side:
    def __init__(self, content):
        #define side content for later use in sympify
        self.content = content

        #separate side into blocks:
        self.blocks = content.split(" + ")

    def update_content(self):
        self.content = ""
        for item in self.blocks:
            if item == self.blocks[-1]:
                self.content = self.content + item
            else:
                self.content = self.content + item + " + "

class Equation:
    def __init__(self, content, subject):
        self.subject = subject
        self.content = content
        #separate eqn into sides
        self.lhs = Side(content.split(" = ")[0])
        self.rhs = Side(content.split(" = ")[1])

        #check if sides should be flipped if subject is on rhs
        for block in self.rhs.blocks:
            if self.subject in block:
                self.flip_sides()

        #checks if the subject block is the only block on LHS
        self.subject_is_isolated = self.is_subject_isolated()

        #checks if subject is the last block on LHS
        self.subject_is_last = self.is_subject_last()   

        #gets subject index
        self.subject_index = self.find_subject_block(self.subject)

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

    def is_subject_isolated(self):
        #checks if the subject block is the only block on LHS
        #assuming subject has already been moved to LHS
        if len(self.lhs.blocks) == 1:
            return True
        else:
            return False
        
    def find_subject_block(self, subject):
        #return index of block containing the subject 
        #assuming subject has already been moved to LHS
        for block in self.lhs.blocks:
            if subject in block:
                return self.lhs.blocks.index(block)

    def is_subject_last(self):
        #checks if subject is the last block
        #assuming subject has been moved to LHS
        #TODO: make this work with a dynamically changing subject
        if self.subject in self.lhs.blocks[-1]:
            return True
        else:
            return False

def main():
    equation = Equation("3*x + 5*z + 23*y = 2 + p", "p") #<----- Modify equation!

    #collect like terms:
    #TODO: code for this. for now assume they have been collected.

    #this will process only addition/subtraction:
    print("original equation:", equation.content)

    #terminate if equation is solved:
    while equation.is_subject_isolated() == False:
        
        #if subject is last, isolate everything except 1st element:
        if equation.is_subject_last() == True:
            subject_list = equation.lhs.blocks[1:]
        #if not, isolate everything except last element
        else:
            subject_list = equation.lhs.blocks[:-1]
        
        #concatenate everything in the isolated list:
        subject_temp = ""
        for item in subject_list:
            if item == subject_list[-1]:
                subject_temp = subject_temp + item
            else:
                subject_temp = subject_temp + item + " + "

        #use sympify to find what needs to be moved from LHS to RHS:
        symbolic_subject = sympify(subject_temp)
        symbolic_lhs = sympify(equation.lhs.content)

        #This works by solving LHS = 0, solving for subject_temp
        #will always be a single solution i.e. a list with one element:
        symbolic_block_to_move = solve(symbolic_lhs, symbolic_subject)[0]

        #this is what should be added to RHS:
        block_to_move_rhs = str(symbolic_block_to_move)
        equation.rhs.blocks.append(block_to_move_rhs)

        #this is what should be removed from the LHS:
        block_to_move_lhs = str(sympify("-1")*symbolic_block_to_move)
        equation.lhs.blocks.remove(block_to_move_lhs)

        #update content for printing
        equation.lhs.update_content()
        equation.rhs.update_content()
        equation.update_content()
        print("STEP:",equation.content)

    print("'solved' equation: ", equation.content)
main()