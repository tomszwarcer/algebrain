import equation
import collect

eq = equation.Equation("6*x + 15 = 12*y + 8*x")
print(collect.collect(eq)[0].content)
