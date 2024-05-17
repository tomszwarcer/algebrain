#need to identify what operations need to be done on the equation

import collect
import equation
import expand
import copy

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
    else:
        return "done"
    
def detect_collect(eq):
    eq_copy = copy.deepcopy(eq)
    if collect.collect(eq_copy)[0].content == eq.content:#very inefficient but it works
        return False
    else:
        return True
    

eq = equation.Equation("3*(2*x + 5) = 4*(3*x + 2)")
subject = "x"
print("Original: " + eq.content)

while next_step(eq,subject) != "done":
    #rewrite all of this
    if next_step(eq,subject) == "expand rhs":
        rhs_old = eq.rhs
        rhs_new = expand.expand(eq.rhs)
        print("expanded rhs " + rhs_old.content + " to " + rhs_new.content + "\n")
        eq.rhs = rhs_new
        eq.update()
    if next_step(eq,subject) == "expand lhs":
        lhs_old = eq.lhs
        lhs_new = expand.expand(eq.lhs)
        print("expanded lhs " + lhs_old.content + " to " + lhs_new.content + "\n")
        eq.lhs = lhs_new
        eq.update()
    if next_step(eq,subject) == "collect":
        eq_new, to_combine_lhs, to_combine_rhs = collect.collect(eq)
        print("collected LHS terms: " + to_combine_lhs + ". RHS terms: " + to_combine_rhs + "\n")

print("final: " + eq_new.content)


