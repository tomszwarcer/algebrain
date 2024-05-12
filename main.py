import collect
import equation

eq = equation.Equation("5*x - y - 2*z + 2 = 4")
print("before: "+ eq.content)
eq = collect.collect(eq)
print("after: " + eq.content)