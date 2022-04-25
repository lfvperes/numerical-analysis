
from types import MethodType
from general import rel_err

# bissection
# linear_iteration
# newton
# secant
# falsi

"""
3. Non linear equations
    3.2. Bisection
    3.3. Linear Iteration
    3.4. Newton
    3.5. Secant
    3.6. Regula-Falsi
    3.7. Non-linear equations systems
        3.7.1. Linear Iteration
        3.7.2. Newton
    3.8. Polynomials
        3.8.1. Real roots
        3.8.2. Complex roots
        3.8.3. Quo-diff
"""

def bisection(a: float, b: float, f: MethodType, epsilon: float) -> float:
    print(f"-------------\nBisection: a = {a}, b = {b}")

    if f(a) * f(b) > 0:
        print(f"No solution")
        return None
    elif f(a) == 0: 
        print(f"a is the root")
        return a
    elif f(b) == 0:
        print(f"b is the root")
        return b

    x_i = (a + b)/2
    if f(x_i) == 0:    
        print(f"Found root x_1 = {x_i}, f(x_1) = {f(x_i)}")
        return x_i

    err = 2 * epsilon
    it_count = 1
    while err >= epsilon:
        it_count += 1
        if f(x_i) * f(a) < 0:
            b = x_i
            x_i = (a + x_i)/2
            err = rel_err(x_i, b)
        elif f(x_i) * f(b) < 0:
            a = x_i
            x_i = (b + x_i)/2
            err = rel_err(x_i, a)

    print(f"Converged after {it_count} iterations:")
    print(f"x_{it_count} = {x_i}, f(x_{it_count}) = {f(x_i)}")
    print(f"error = {err} < {epsilon}")

    return x_i

def eq_lin_it(f: MethodType, psi: MethodType, x_0: float, epsilon: float)-> float:
    print(f"-------------\nLinear Iteration (for equations): x_0 = {x_0}")

    if f(x_0) == 0:    
        print(f"Found root x_1 = {x_0}, f(x_1) = {f(x_0)}")
        return x_0

    err = 2 * epsilon
    it_count = 0
    while err >= epsilon:
        it_count += 1
        x_i = psi(x_0)
        err = rel_err(x_i, x_0)
        x_0 = x_i
    
    print(f"Converged after {it_count} iterations:")
    print(f"x_{it_count} = {x_i}, f(x_{it_count}) = {f(x_i)}")
    print(f"error = {err} < {epsilon}")

    return x_i

def eq_newton():
    print("")
    

def sys_lin_it(): # systems
    print("linear iteration - system of equations")

# systems
def sys_newton(p_0: list[float, float], max_err: float, f: MethodType, f_x: MethodType, f_y: MethodType, g: MethodType, g_x: MethodType, g_y: MethodType):
    """ Newton's method for non-linear equations systems

    Parameters
    ----------
    p_0 : list[float, float]
        coordinates (x_0, y_0), approximation for the solution (x, y) of the system
    max_err : float
        _description_
    f : MethodType
        _description_
    f_x : MethodType
        _description_
    f_y : MethodType
        _description_
    g : MethodType
        _description_
    g_x : MethodType
        _description_
    g_y : MethodType
        _description_
    """
    
    print(f"-------------\nNewton's Method (for non-linear systems): p_0 = {p_0}")
    x_1, y_1 = p_0
    err_x, err_y = 2 * max_err, 2 * max_err
    i = 0
    
    while err_x > max_err or err_y > max_err:
        x_0 = x_1
        y_0 = y_1

        f_0 = f(x_0, y_0)
        f_x0 = f_x(x_0, y_0)
        f_y0 = f_y(x_0, y_0)

        g_0 = g(x_0, y_0)
        g_x0 = g_x(x_0, y_0)
        g_y0 = g_y(x_0, y_0)

        J = f_x0 * g_y0 - f_y0 * g_x0
        
        x_1 = x_0 - (f_0 * g_y0 - f_y0 * g_0)/J
        y_1 = y_0 - (g_0 * f_x0 - g_x0 * f_0)/J

        err_x = abs(x_1 - x_0) / max(1, abs(x_1))
        err_y = abs(y_1 - y_0) / max(1, abs(y_1))

        i += 1
        print(f"\nIteration {i}:")
        print(f"J = {J}")
        print(f"x_1 = {x_1}, y_1 = {y_1}")
        print(f"err_x = {err_x}, err_y = {err_y}")

        if i > 100:
            print("No solution")
            break
