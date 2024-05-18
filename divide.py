#only to be used when LHS has subject block isolated

import sympy as sp


def divide(eq, subject):
    to_multiply = str(sp.solve(eq.lhs.content + " - 1", subject)[0])
    new_lhs = eq.lhs.content + "*(" + to_multiply + ")"
    new_rhs = "(" + eq.rhs.content + ")" + "*(" + to_multiply + ")"
    eq.lhs.content = str(sp.sympify(new_lhs))
    eq.rhs.content = new_rhs
    eq.lhs.create_blocks_signs()
    eq.rhs.create_blocks_signs()
    eq.update()
    return eq, to_multiply
