#takes as input an expression
#expands a single bracket

#looks through the expression until it finds a bracket
#and then expands everything before the bracket with said bracket

#supports a single nested bracket inside the outside bracket
#e.g. 2*(3*(2*z + 1) + 2*x) but not 2*(3*(2*z + 1) + 2*(3*x + 4))

#For some reason it doesn't work if we use "O" or "Q" instead of "i" as the nest sub

import sympy as sp
import expression

def expand(input_exp):
    de_nested_content, nest = de_nest(input_exp)
    if nest == "":
        expanded_nested = sp.expand(de_nested_content)
        return expression.Expression(str(expanded_nested))
    else: 
        expanded_nested = sp.expand(de_nested_content) 
        return expression.Expression(re_nest(str(expanded_nested), nest))
    
def de_nest(exp):
    #returns de-nested content
    #look for nested brackets
    nested = False
    bracket_num = 0
    holder = ""
    #replace with char?
    for i in range(len(exp.content)):
        if exp.content[i] == "(":
            bracket_num += 1
            if bracket_num == 2:
                nested = True
                open_nest = i
        if exp.content[i] == ")":
            #add in the last nested bracket:
            if bracket_num == 2:
                close_nest = i
                holder += exp.content[i]
            bracket_num -= 1

        #nested case:
        if bracket_num == 2:
            holder += exp.content[i]
    #don't de nest if not nested:
    if not nested:
        return exp.content, ""
    else:
        nest = exp.content[open_nest:close_nest + 1]
        #use "i" as nest substituion as it is unlikely to be used in an equation.    
        de_nest = exp.content[:open_nest] + "i" + exp.content[close_nest+1:] 
        return de_nest, nest

def re_nest(de_nested_content, nest):
    split = de_nested_content.split("i")
    join = nest.join(split)
    return join

#unused but may be useful later:
def isolate_inside(string):
    #look for nested brackets
    bracket_num = 0
    holder = ""
    #maybe replace with char?
    for i in range(len(string)):
        if string[i] == "(":
            bracket_num += 1
            if bracket_num == 1:
                open_bra = i
        if string[i] == ")":
            #add in the last nested bracket:
            if bracket_num == 1:
                close_bra = i
                holder += string[i]
            bracket_num -= 1

        #nested case:
        if bracket_num == 1:
            holder += string[i]
    #exclude brackets:
    inside = string[open_bra+ 1:close_bra]
    
    return inside  