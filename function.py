import sympy

x = sympy.Symbol('x')

func = x**3
func_der = func.diff(x)
func_int = func.integrate(x)

print(func_int, func, func_der)

f = sympy.lambdify(x, func)
fd = sympy.lambdify(x, func_der)
fi = sympy.lambdify(x, func_int)

print(f(2))
print(fd(2))
print(fi(2))