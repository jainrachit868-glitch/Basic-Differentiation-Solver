import math

def power_rule(n, x):
    return n * (x**(n-1))

def exp_rule(x):
    return math.exp(x)

def log_rule(x):
    return 1/x

def constant_rule(c):
    return 0

# Trigonometric rules
def d_sin(x):
    return math.cos(x)

def d_cos(x):
    return -math.sin(x)

def d_tan(x):
    return 1 / (math.cos(x)**2)  

def d_cot(x):
    return -(1 / (math.sin(x)**2))  

# Inverse trigonometric rules
def d_arcsin(x):
    return 1 / math.sqrt(1 - x**2)

def d_arccos(x):
    return -1 / math.sqrt(1 - x**2)

def d_arctan(x):
    return 1 / (1 + x**2)

def d_arccot(x):
    return -1 / (1 + x**2)

def d_arcsec(x):
    return 1 / (abs(x) * math.sqrt(x**2 - 1))

def d_arccsc(x):
    return -1 / (abs(x) * math.sqrt(x**2 - 1))

# Dispatcher function
def differentiate(expr_str, x_value):
    if expr_str == "sin(x)":
        return d_sin(x_value)
    elif expr_str == "cos(x)":
        return d_cos(x_value)
    elif expr_str == "tan(x)":
        return d_tan(x_value)
    elif expr_str == "cot(x)":
        return d_cot(x_value)
    elif expr_str == "arcsin(x)":
        return d_arcsin(x_value)
    elif expr_str == "arccos(x)":
        return d_arccos(x_value)
    elif expr_str == "arctan(x)":
        return d_arctan(x_value)
    elif expr_str == "arccot(x)":
        return d_arccot(x_value)
    elif expr_str == "arcsec(x)":
        return d_arcsec(x_value)
    elif expr_str == "arccsc(x)":
        return d_arccsc(x_value)
    elif expr_str == "exp(x)":
        return exp_rule(x_value)
    elif expr_str == "log(x)":
        return log_rule(x_value)
    elif expr_str.startswith("x**"):
        n = int(expr_str.split("**")[1])
        return power_rule(n, x_value)
        return power_rule(n, x_value)
    elif expr_str.isdigit():
        return constant_rule(int(expr_str))
    else:
        return "Rule not implemented"
