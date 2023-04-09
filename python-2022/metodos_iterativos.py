"""Aula 5 - 04/04/2022
Métodos iterativos
Luís Filipe Vasconcelos Peres
"""
import numpy as np

def jacobi(A, b, max_err):
    N = len(A)
    As = np.zeros(N)
    bs = np.zeros(N,1)
    for i in list(range(1, N)):
        for j in list(range(1, N)):
            As[i, j] = A[i, j] / A[i, i]
        
        bs[i] = b[i] / A[i, i]
    
    soma = 0
    # criterio de linhas
    for i in list(range(1, N)):
        soma = 0
        for j in list(range(1, N)):
            if (i != j):
                soma += As[i, j]
        
        alphac[1, j] = soma
    if (max(alphal) < 1 or max(alphac) < 1):
        x = met_jacobi(A, b, err_max)
    else: return

def met_jacobi(As, bs, max_err):
    N = len(As)
    B = -As + np.eye(N) #???
    

    for i in range(N):
        for j in range(N):
            B[i,j]