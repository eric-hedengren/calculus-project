import sympy

def derivative_check(function, answer):
    form_der = sympy.sympify(function).diff(x)
    form_ans = sympy.sympify(answer)

    if form_der == form_ans:
        return str(form_der)

def integral_check(function, answer):
    form_int = sympy.sympify(function).integrate(x)
    form_ans = sympy.sympify(answer)

    if form_int == form_ans:
        return str(form_int)

def function_point(function):
    return sympy.lambdify(x, function)

x = sympy.Symbol('x')