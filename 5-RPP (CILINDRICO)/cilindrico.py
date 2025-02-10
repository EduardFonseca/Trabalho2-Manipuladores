import sys
import os
# Add the parent directory to the system path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from model_tools import *
from auxiliar_plots import *
import numpy as np
import sympy as sp

if __name__ == '__main__':
    # Robô CILINDRICO:
    # |========================================|
    # | Ai | d       | theta     | a   | alpha |
    # |----|---------|-----------|-----|-------|
    # | A1 | L1      |  th1*    | 0   | 0     |
    # | A2 | L2 + d2*|  -90     | 0   | -90   |
    # | A3 | d3*     |  0       | 0   | 0     |
    # |========================================|

    if(input("Deseja usar a matriz de transformação homogênea genérica? (s/n): ") == 's'):
        #Definindo os parâmetros do robô:
        # Joint variables

        th1, th2, l1, l2, d2, d3 = sp.symbols('th1 th2 l1 l2 d2 d3', real=True)

        # Matriz de transformação homogênea
        F0 = np.eye(4)

        A1 = A.subs([(d, l1), (theta, th1), (a, 0), (alpha, 0)])
        F1 = sp.simplify(F0 @ A1)

        A2 = A.subs([(d, l2+d2), (theta, np.deg2rad(-90)), (a, 0), (alpha, np.deg2rad(-90))])
        F2 = sp.simplify(F1 @ A2)

        A3 = A.subs([(d, d3), (theta, 0), (a, 0), (alpha, 0)])
        F3 = sp.simplify(F2 @ A3)

        print(sp.latex(sp.simplify(F3)))
        print(sp.pretty(sp.simplify(F3)))

    # Fazendo o calculo numerico
    L1, L2 = 1, 1# links fixos
    D2, D3 = 0, 0 # deslocamentos
    TH1 = np.deg2rad(0) # angulos

    f0 = np.eye(4)
    f1 = f0 @ numeric_DH(L1, TH1, 0, 0)
    f2 = f1 @ numeric_DH(L2+D2, np.deg2rad(-90), 0, np.deg2rad(-90))
    f3 = f2 @ numeric_DH(D3, 0, 0, 0)

    frames = [f0, f1, f2, f3]

    # Plotando o robô na posicao zero
    plt.figure(1)
    fig = plt.axes(projection='3d')
    plot_robot(fig, frames, origin=True)

    #Posicao aleatoria
    D2, D3 = 1, 1 # deslocamentos
    TH1 = np.deg2rad(45) # angulos

    f0 = np.eye(4)
    f1 = f0 @ numeric_DH(L1, TH1, 0, 0)
    f2 = f1 @ numeric_DH(L2+D2, np.deg2rad(-90), 0, np.deg2rad(-90))
    f3 = f2 @ numeric_DH(D3, 0, 0, 0)

    frames = [f0, f1, f2, f3]

    # Plotando o robô na posicao zero
    plt.figure(2)
    fig2 = plt.axes(projection='3d')
    plot_robot(fig2, frames, origin=True, show=True)


