import expression
import multiply

b1 = expression.Expression("3 + x")
b2 = expression.Expression("2 + y")

print(multiply.multiply(b1,b2).content)
