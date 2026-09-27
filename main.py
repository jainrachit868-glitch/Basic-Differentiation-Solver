import operators

print("Differentiation Calculator")

expr = input("Enter function: ")
x = float(input("Enter value of x: "))

answer = operators.differentiate(expr, x)

print("Derivative value =", answer)