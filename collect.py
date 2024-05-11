#given an equation, collect like terms
#deal with numbers or algebra
#should be no brackets in this step so no need to implement bracket support.
#TODO: add ability to report which terms were combined and the result


import equation
import block
import sympy as sp

def collect(equation):

    #create list of block algebra parts
    alg_parts = []
    #create list of algebra parts that repeat (INEFFICIENT)
    common_algs = []
    #if common_algs contains "" then there are numbers to collect.
    for i in equation.all_blocks:
        if i.alg in alg_parts:
            common_algs.append(i.alg)
        alg_parts.append(i.alg)

    if common_algs == []:
        print("Nothing to collect")
        return equation
    else:
        to_combine_lhs = []
        to_combine_rhs = []
        to_remove_lhs = []
        to_remove_rhs = []
        #will only deal with the 1st entry in common_algs in each iteration
        #the program needs to be run multiple times.
        for i in range(len(equation.lhs.blocks)):
            if equation.lhs.blocks[i].alg == common_algs[0]:
                to_combine_lhs.append(equation.lhs.blocks[i])
                to_remove_lhs.append(equation.lhs.blocks[i])

        for i in range(len(equation.rhs.blocks)):
            if equation.rhs.blocks[i].alg == common_algs[0]:
                to_combine_rhs.append(equation.rhs.blocks[i])
                to_remove_rhs.append(equation.rhs.blocks[i])

        #remove what needs to be removed:
        for i in to_remove_lhs:
            if i in equation.lhs.blocks:
                equation.lhs.blocks.remove(i)

        
        for i in to_remove_rhs:
            if i in equation.rhs.blocks:
                equation.rhs.blocks.remove(i)

        #deal with case of nothing to combine from one side:
        if to_combine_lhs == []:
            common_equation_lhs = "0"
        else:
            common_equation_lhs = block.Block.blocks_to_str(to_combine_lhs)
        if to_combine_rhs == []:
            common_equation_rhs = "0"
        else:
            common_equation_rhs = block.Block.blocks_to_str(to_combine_rhs)    

        #simplify:
        common_expr = sp.sympify(common_equation_lhs) - sp.sympify(common_equation_rhs)
        common_expr = block.Block.str_to_block(str(common_expr))

        #add to LHS:
        equation.lhs.blocks.append(common_expr)

        #update everything:
        equation.lhs.update()
        equation.rhs.update()
        equation.update()

        return equation


            



