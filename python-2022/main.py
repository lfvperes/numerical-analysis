from non_linear_equations import *
from linear_systems_exact import *
from numpy import exp

def f(x,y): return x ** 2 + y ** 2 - 2

def f_x(x,y): return 2 * x

def f_y(x,y): return 2 * y

def g(x,y): return x ** 2 - y ** 2 - 1

def g_x(x,y): return 2 * x

def g_y(x,y): return -2 * y


# newton([1.1, 0.8], 1e-1, f, f_x, f_y, g, g_x, g_y)
sys_newton(
    [1.1, 0.8],                     # p_0 = [x_0, y_0]
    1e-1,                           # max_err
    lambda x, y: x**2 + y**2 - 2,   # f(x, y)
    lambda x, y: 2*x,               # f_x(x, y)
    lambda x, y: 2*y,               # f_y(x, y)
    lambda x, y: x**2 - y**2 - 1,   # g(x, y)
    lambda x, y: 2*x,               # g_x(x, y)
    lambda x, y: -2*y,              # g_y(x, y)
    )

x = bisection(
    0,                                      # a
    1,                                      # b
    lambda x: (x+1)**2 * exp(x**2-2) - 1,   # f(x)
    1e-4                                    # max_err
    )

ans_lin_it = eq_lin_it(
    lambda x: x**2 - x - 2,
    lambda x: (2 + x)**(1/2),
    2.5,
    1e-4
)

gauss_elim(
    np.array([
        [6, 2, -1],
        [2, 4, 1],
        [3, 2, 8]
        ], dtype=float),
    np.array([[7], [7], [13]], dtype=float)
    # np.array([[7, 7, 13]], dtype=float)
)