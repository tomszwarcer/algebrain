def flip(eq):
    rhs_temp = eq.rhs
    eq.rhs = eq.lhs
    eq.lhs = rhs_temp
    eq.update()
    return eq