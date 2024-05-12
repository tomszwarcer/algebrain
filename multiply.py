#takes as input two Exp objects 
#multiplies them with sympy
#returns Exp object
#quick and dirty multiplication

import block
import expression
import sympy as sp

def multiply(exp1,exp2):
    product = sp.expand("(" + exp1.content + ")" + "*" + "(" + exp2.content +")")
    return expression.Expression(str(product))
