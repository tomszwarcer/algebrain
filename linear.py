from sympy import *

#Solves linear equations
#in its current form, isolates whatever has an 'x' in it. Can't collect terms or divide.
#Can deal with negative coefficients!
#TODO: add collecting like terms functionality
#TODO: implement division
#TODO: give some indication when original equation has been flipped
#TODO: implement sanitisation. Currently only works with spaces around all signs.

class Side:
    def __init__(self, content):
        #define side content for later use in sympify
        self.content = content

        #separate side into blocks: this list includes signs only at instantiation of Side.
        self.blocks = self.content.split(" ")

        #create signs list: 
        self.signs = []

        #special behaviour for 1st element:
        #if no sign on 1st elememt default to plus
        if self.blocks[0] != "-" and self.blocks[0] != "+":
            self.blocks.insert(0, "+")

        #assign signs and remove them from block
        self.signs = self.blocks[0::2]
        del self.blocks[0::2]

    def update(self):
        #update content from blocks
        self.content = ""
        #construct content from blocks using signs:
        for index in range(len(self.blocks)):
            if self.signs[index] == "+":    
                if index == len(self.blocks) - 1:
                    self.content = self.content + self.blocks[index]
                else:
                    self.content = self.content + self.blocks[index] + " + "
            else:
                if index == len(self.blocks) - 1:
                    self.content = self.content + "- " + self.blocks[index]
                else:
                    self.content = self.content + "- " + self.blocks[index] + " + "
        
        #simplify any '+ -':
        if "+ - " in self.content:
            split_content = self.content.split(" + - ")
            self.content = ""
            for item in split_content:
                if item == split_content[-1]:
                    self.content = self.content + item
                else:
                    self.content = self.content + item + " - "

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

    def update(self):
        # updates the written form of equation (for use with SymPy)
        self.content = self.lhs.content + " = " + self.rhs.content

    def flip_sides(self):
        # function to flip sides, e.g. to put subject on LHS
        temp = self.lhs
        self.lhs = self.rhs
        self.rhs = temp

        #update equation content:
        self.update()

    def is_subject_isolated(self):
        #checks if the subject block is the only block on LHS
        #assuming subject has already been moved to LHS
        if len(self.lhs.blocks) == 1:
            return True
        else:
            return False

    def is_subject_last(self):
        #checks if subject is the last block
        #assuming subject has been moved to LHS
        #TODO: make this work with a dynamically changing subject
        if self.subject in self.lhs.blocks[-1]:
            return True
        else:
            return False

def main():
    equation = Equation("- 2*y + 1 = x", "y") #<----- Modify equation!

    #collect like terms:
    #TODO: code for this. for now assume they have been collected.

    #this will process only addition/subtraction:
    print("original equation:", equation.content)

    #terminate if equation is solved:
    while equation.is_subject_isolated() == False:
        
        #if subject is last, isolate everything except 1st element:
        if equation.is_subject_last() == True:
            subject_list = equation.lhs.blocks[1:]
            subject_signs = equation.lhs.signs[1:]
        #if not, isolate everything except last element
        else:
            subject_list = equation.lhs.blocks[:-1]
            subject_signs = equation.lhs.signs[:-1]
        #concatenate everything in the isolated list to form subject:
        #+ - will get simplified down
        subject_temp = ""
        for index in range(len(subject_list)):
            if subject_signs[index] == "+":
                if index == len(subject_list) - 1:
                    subject_temp = subject_temp + subject_list[index]
                else:
                    subject_temp = subject_temp + subject_list[index] + " + "
            else:
                if index == len(subject_list) - 1:
                    subject_temp = subject_temp + "-" + subject_list[index]
                else:
                    subject_temp = subject_temp + "-" + subject_list[index] + " + "

        #use sympify to find what needs to be moved from LHS to RHS:
        symbolic_subject = sympify(subject_temp)
        symbolic_lhs = sympify(equation.lhs.content)

        #This works by solving LHS = 0, solving for subject_temp
        #will always be a single solution i.e. a list with one element:
        symbolic_block_to_move = solve(symbolic_lhs, symbolic_subject)[0]

        #this is what should be added to RHS:
        block_to_move_rhs = str(symbolic_block_to_move)
        if block_to_move_rhs[0] == "-":
            block_to_move_rhs = block_to_move_rhs[1:]
            equation.rhs.signs.append("-")
        else:
            equation.rhs.signs.append("+")
        equation.rhs.blocks.append(block_to_move_rhs)
        

        #this is what should be removed from the LHS:
        block_to_move_lhs = str(sympify("-1")*symbolic_block_to_move)

        #remove corresponding sign which may be added
        if block_to_move_lhs[0] == "-":
            block_to_move_lhs = block_to_move_lhs[1:]
        del equation.lhs.signs[equation.lhs.blocks.index(block_to_move_lhs)]
        equation.lhs.blocks.remove(block_to_move_lhs)

        #update content for printing
        equation.lhs.update()
        equation.rhs.update()
        equation.update()
        print("STEP:",equation.content)

    print("'solved' equation: ", equation.content)
main()