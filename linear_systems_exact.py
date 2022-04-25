import numpy as np
from types import MethodType
from general import rel_err

"""
4. Linear Systems
    4.x. blablabla
        4.x.y. bla
    4.5. Gauss' Elimination
"""


# def gauss_elim(A: np.ndarray, b: np.ndarray) -> np.ndarray:
#     return gauss_elim(np.concatenate(A, b))

def gauss_elim(A: np.ndarray, b: np.ndarray=None) -> np.ndarray:
# def gauss_elim(A: np.ndarray) -> np.ndarray:
    """Gauss' Elimination Method or "Simple Gauss' Method" for solving the Linear System Ax = b. Consists on replacing an equation by the difference between itself and another equation (both from different lines in the given system), multiplied by a non-zero constant.

    Parameters
    ----------
    A : np.ndarray
        Matrix of coefficients NxN such that det(A_k) != 0, k = 1, 2, ..., N
    b : np.ndarray
        Independant term vector Nx1

    Returns
    -------
    np.ndarray
        Vector x, solution to the system Ax=b
    """
    print(f"-------------\nGauss' Elimination Method (for linear systems Ax=b)")

    N = len(A)
    if b is not None:
        S = np.concatenate((A,b), axis=1)
        print(f"A={A}\nb={b}")
    else:
        S = A
        print("A|b={S}")
    
    for k in range(N-1):
        for i in range(k+1,N):
            S[i] = S[i] - S[k] * S[i][k]/S[k][k]
    
    x = np.array(b*0)

    for i in range(N-1, -1, -1):
        x[i] = (S[i][-1] - np.matmul(S[i][:-1], x))/S[i][i]
    
    for i in range(N):
        print(f"x_{i} = {x[i][0]:}")
    
    return x

    
    