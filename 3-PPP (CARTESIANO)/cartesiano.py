import sys
import os
# Add the parent directory to the system path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from model_tools import *
from auxiliar_plots import *
import numpy as np
import sympy as sp

if __name__ == '__main__':
    # Robô CARTESIANO:
    # |========================================|
    # | Ai | d       | theta     | a   | alpha |
    # |----|---------|-----------|-----|-------|
    # | A1 | L0      |  0        | 0   | -90   |
    # | A2 | L1 + d1*| -90       | 0   | -90   |
    # | A3 | L2 + d2*|  90       | 0   | -90   |
    # | A4 | d3*     |  0        | 0   |  0    |
    # |========================================|

    if(input("Deseja usar a matriz de transformação homogênea genérica? (s/n): ") == 's'):
        # Definindo os parâmetros do robô:
        # Joint variables
        d1, d2, d3, l0, l1, l2 = sp.symbols('d1 d2 d3 l0 l1 l2', real=True)

        # Matriz de transformação homogênea
        F0 = np.eye(4)

        A1 = A.subs([(d, l0), (theta, 0), (a, 0), (alpha, np.deg2rad(-90))])
        F1 = sp.simplify(F0 @ A1)

        A2 = A.subs([(d, l1 + d1), (theta, np.deg2rad(-90)), (a, 0), (alpha, np.deg2rad(-90))])
        F2 = sp.simplify(F1 @ A2)

        A3 = A.subs([(d, l2 + d2), (theta, np.deg2rad(90)), (a, 0), (alpha, np.deg2rad(-90))])
        F3 = sp.simplify(F2 @ A3)

        A4 = A.subs([(d, d3), (theta, 0), (a, 0), (alpha, 0)])
        F4 = sp.simplify(F3 @ A4)

        print(sp.latex(sp.simplify(F4)))
        print(sp.pretty(sp.simplify(F4)))

    # Fazendo o calculo numerico
    L0, L1, L2 = 1, 1, 1 # links fixos
    d1, d2, d3 = 0, 0, 0 # deslocamentos

    f0 = np.eye(4)
    f1 = f0 @ numeric_DH(L0, 0, 0, np.deg2rad(-90))
    f2 = f1 @ numeric_DH(L1 + d1, np.deg2rad(-90), 0, np.deg2rad(-90))
    f3 = f2 @ numeric_DH(L2 + d2, np.deg2rad(90), 0, np.deg2rad(-90))
    f4 = f3 @ numeric_DH(d3, 0, 0, 0)

    frames = [f0, f1, f2, f3, f4]

    # Plotando o robô na posicao zero
    plt.figure(1)
    fig = plt.axes(projection='3d')

    plot_robot(fig, frames, origin=True)

    #Frame arbitrario
    d1, d2, d3 = 1, 1, 1 # deslocamentos

    f0 = np.eye(4)
    f1 = f0 @ numeric_DH(L0, 0, 0, np.deg2rad(-90))
    f2 = f1 @ numeric_DH(L1 + d1, np.deg2rad(-90), 0, np.deg2rad(-90))
    f3 = f2 @ numeric_DH(L2 + d2, np.deg2rad(90), 0, np.deg2rad(-90))
    f4 = f3 @ numeric_DH(d3, 0, 0, 0)

    frames = [f0, f1, f2, f3, f4]

    # Plotando o robô na posicao zero
    plt.figure(2)
    fig2 = plt.axes(projection='3d')

    plot_robot(fig2, frames, origin=True, show = True)