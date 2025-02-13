import sys
import os
# Add the parent directory to the system path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from model_tools import *
from auxiliar_plots import *
import numpy as np
import sympy as sp

if __name__ == '__main__':
    # Robô PLANAR RRP:
    # |========================================|
    # | Ai | d       | theta     | a   | alpha |
    # |----|---------|-----------|-----|-------|
    # | 1  | 0       | th1*      | L1  | 0     |
    # | 2  | 0       | 90 + th2* | 0   | 90    |
    # | 3  | L2 + d3*| 0         | 0   | 0     |
    # |========================================|

    # Definindo os parâmetros do robô:

    if(input("Deseja usar a matriz de transformação homogênea genérica? (s/n): ") == 's'):
        # Joint variables
        th1, th2, l1, l2, d3 = sp.symbols('th1 th2 l1 l2 d3', real=True)
        
        # Matriz de transformação homogênea
        F0 = np.eye(4)
        
        A1 = A.subs([(d, 0), (theta, th1), (a, l1), (alpha, 0)])
        F1 = sp.simplify(F0 @ A1)

        A2 = A.subs([(d, 0), (theta, np.deg2rad(90)+th2), (a, 0), (alpha, np.deg2rad(90))])
        F2 = sp.simplify(F1 @ A2)

        A3 = A.subs([(d, l2+d3), (theta, 0), (a, 0), (alpha, 0)])
        F3 = sp.simplify(F2 @ A3)

        print(sp.latex(sp.simplify(F3)))
        print(sp.pretty(sp.simplify(F3)))

    # Fazendo o calculo numerico, devido a eficiência
    L1, L2= 1, 1 # links fixos
    D3 = 1 # link variável
    TH1, TH2 = np.deg2rad(0), np.deg2rad(0)
    
    f0 = np.eye(4)
    f1 = f0 @ numeric_DH(0, TH1, L1, 0)
    f2 = f1 @ numeric_DH(0, np.deg2rad(90)+TH2, 0, np.deg2rad(90))
    f3 = f2 @ numeric_DH(L2+D3, 0, 0, 0)

    frames = [f0, f1, f2, f3]

    # Plotando o robô na posicao zero
    plt.figure(1)
    fig = plt.axes(projection='3d')

    plot_robot(fig, frames, origin=True)

    # Plotando a transição de um frame para o outro
    plt.figure(2)
    fig2 = plt.axes(projection='3d')

    D3 = 2 # link variável
    TH1, TH2 = np.deg2rad(90), np.deg2rad(-90)

    f0 = np.eye(4)
    f1 = f0 @ numeric_DH(0, TH1, L1, 0)
    f2 = f1 @ numeric_DH(0, np.deg2rad(90)+TH2, 0, np.deg2rad(90))
    f3 = f2 @ numeric_DH(L2+D3, 0, 0, 0)

    frames = [f0, f1, f2, f3]

    plot_robot(fig2, frames, origin=True, show=True)




