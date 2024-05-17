import expression
import equation
import expand
import flip
import move
import collect


eq = equation.Equation("-x + 6*y + 7 = 12*x")

print(collect.collect(eq)[0].content)
