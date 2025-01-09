import sys
import os
# Add the parent directory to the system path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from model_tools import *
from auxiliar_plots import *
import numpy as np
import sympy as sp

if __name__ == '__main__':
    # Robô SCARA:
    # |========================================|
    # | Ai | d       | theta     | a   | alpha |
    # |----|---------|-----------|-----|-------|
    # | A1 | L1z      |  th1*    | L1x | 0     |
    # | A2 | 0        |  th2*    | L2  | 180   |
    # | A3 | d3*      |  0       | 0   | 0     |
    # |========================================|

    if(input("Deseja usar a matriz de transformação homogênea genérica? (s/n): ") == 's'):
        #Definindo os parâmetros do robô:
        # Joint variables

        l1z, th1, l1x, th2, l2, d3 = sp.symbols('l1z th1 l1x th2 l2 d3', real=True)

        # Matriz de transformação homogênea
        F0 = np.eye(4)

        A1 = A.subs([(d, l1z), (theta, th1), (a, l1x), (alpha, 0)])
        F1 = sp.simplify(F0 @ A1)

        A2 = A.subs([(d, 0), (theta, th2), (a, l2), (alpha, np.deg2rad(180))])
        F2 = sp.simplify(F1 @ A2)

        A3 = A.subs([(d, d3), (theta, 0), (a, 0), (alpha, 0)])
        F3 = sp.simplify(F2 @ A3)

        print(sp.latex(sp.simplify(F3)))
        print(sp.pretty(sp.simplify(F3)))

    # Fazendo o calculo numerico
    L1Z, L1X, L2 = 1, 1, 1 # links fixos
    D3 = 0 # deslocamentos
    TH1, TH2 = np.deg2rad(0), np.deg2rad(0) # angulos

    f0 = np.eye(4)
    f1 = f0 @ numeric_DH(L1Z, TH1, L1X, 0)
    f2 = f1 @ numeric_DH(0, TH2, L2, np.deg2rad(180))
    f3 = f2 @ numeric_DH(D3, 0, 0, 0)

    frames = [f0, f1, f2, f3]

    # Plotando o robô na posicao zero
    plt.figure(1)
    fig = plt.axes(projection='3d')
    plot_robot(fig, frames, origin=True)

    #Posicao aleatoria
    D3 = 1 # deslocamentos
    TH1, TH2 = np.deg2rad(40), np.deg2rad(45) # angulos

    f0 = np.eye(4)
    f1 = f0 @ numeric_DH(L1Z, TH1, L1X, 0)
    f2 = f1 @ numeric_DH(0, TH2, L2, np.deg2rad(180))
    f3 = f2 @ numeric_DH(D3, 0, 0, 0)

    frames = [f0, f1, f2, f3]

    # Plotando o robô na posicao zero
    plt.figure(2)
    fig2 = plt.axes(projection='3d')
    plot_robot(fig2, frames, origin=True, show=True)


