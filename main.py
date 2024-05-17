#need to identify what operations need to be done on the equation

import collect
import equation
import expand
import copy
import flip
import move

def detect_expand(exp):
    for char in exp.content:
        if char == "(":
            return True
    return False

def next_step(eq,subject):
    #if rhs needs expanding:
    if detect_expand(eq.rhs):
        return "expand rhs"
    elif detect_expand(eq.lhs):
        return "expand lhs"
    elif detect_collect(eq):
        return "collect"
    elif detect_move(eq,subject):
        return "move"
    elif detect_flip(eq,subject):
        return "flip"
    else:
        return "done"
    
def detect_collect(eq):
    eq_copy = copy.deepcopy(eq)
    if collect.collect(eq_copy)[0].content == eq.content:#very inefficient but it works
        return False
    else:
        return True
    
def detect_flip(eq,subject):
    #detects when we should flip the sides
    #should be used only after expand/collect and move
    for block in eq.rhs.blocks:
        if subject in block.content:
            return True
    return False
    
def detect_move(eq,subject):
    subj_block, subj_side = move.get_subj_block(eq, subject)
    if move.is_subject_isolated(eq,subj_side) == False:
        return True
    elif subj_block.sign == "-":
        #going here even for positive...?
        return True
    else:
        return False
    

eq = equation.Equation("3*(2*y + 5) - x = 4*(3*x + 2)")
subject = "x"
print("Original: " + eq.content+ "\n")

while next_step(eq,subject) != "done":
    #rewrite all of this
    if next_step(eq,subject) == "expand rhs":
        rhs_old = eq.rhs
        rhs_new = expand.expand(eq.rhs)
        print("expanded rhs " + rhs_old.content + " to " + rhs_new.content)
        eq.rhs = rhs_new
        eq.update()
        print("current: " + eq.content+ "\n")
    elif next_step(eq,subject) == "expand lhs":
        lhs_old = eq.lhs
        lhs_new = expand.expand(eq.lhs)
        print("expanded lhs " + lhs_old.content + " to " + lhs_new.content)
        eq.lhs = lhs_new
        eq.update()
        print("current: " + eq.content+ "\n")
    elif next_step(eq,subject) == "collect":
        eq_new, to_combine_lhs, to_combine_rhs = collect.collect(eq)
        print("collected LHS terms: " + to_combine_lhs + ". RHS terms: " + to_combine_rhs)
        eq = eq_new
        print("current: " + eq.content+ "\n")
    elif next_step(eq,subject) == "move":
        eq_new = copy.deepcopy(eq)
        eq_new, subj_side, subj_block = move.move(eq_new,subject)
        print("moved " + subj_block.content + " to " + subj_side)
        eq = eq_new
        print("current: " + eq.content+ "\n")
    elif next_step(eq,subject) == "flip":
        eq_new = copy.deepcopy(eq)
        eq_new = flip.flip(eq_new)
        print("flipped " + eq.content + " to " + eq_new.content)
        eq = eq_new
        print("current: " + eq.content+ "\n")

print("final: " + eq_new.content)


