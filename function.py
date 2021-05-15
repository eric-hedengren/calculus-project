import sympy

def derivative_check(function, answer):
    form_func = sympy.sympify(function)
    func_der = form_func.diff(x)

    form_ans = sympy.sympify(answer)

    if func_der == form_ans:
        return True
    else:
        return False

def integral_check(function, answer):
    form_func = sympy.sympify(function)
    func_int = form_func.integrate(x)

    form_ans = sympy.sympify(answer)

    if func_int == form_ans:
        return True
    else:
        return False

x = sympy.Symbol('x')