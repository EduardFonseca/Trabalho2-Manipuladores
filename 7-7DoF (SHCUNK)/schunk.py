import sys
import os
# Add the parent directory to the system path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from model_tools import *
from auxiliar_plots import *
import numpy as np
import sympy as sp

if __name__ == '__main__':
    # Robô SCHUNK:
    # |========================================|
    # | Ai | d       | theta     | a   | alpha |
    # |----|---------|-----------|-----|-------|
    # | A1 | L1      | th1*      | 0   | 90    |
    # | A2 | 0       | th2*      | 0   |-90    |
    # | A3 | L2      | th3*      | 0   | 90    |
    # | A4 | 0       | th4*      | 0   |-90    |
    # | A5 | L3      | th5*      | 0   | 90    |
    # | A6 | 0       | th6*      | 0   |-90    |
    # | A7 | L4      | th7*      | 0   | 0     |
    # |========================================|

    if(input("Deseja usar a matriz de transformação homogênea genérica? (s/n): ") == 's'):
        # Definindo os parâmetros do robô:
        # Joint variables
        th1, th2, th3, th4, th5, th6, th7, l1, l2, l3, l4 = sp.symbols('th1 th2 th3 th4 th5 th6 th7 l1 l2 l3 l4', real=True)

        F0 = np.eye(4)

        A1 = A.subs([(d, l1), (theta, th1), (a, 0), (alpha, np.deg2rad(90))])
        F1 = sp.simplify(F0 @ A1)

        A2 = A.subs([(d, 0), (theta, th2), (a, 0), (alpha, np.deg2rad(-90))])
        F2 = sp.simplify(F1 @ A2)

        A3 = A.subs([(d, l2), (theta, th3), (a, 0), (alpha, np.deg2rad(90))])
        F3 = sp.simplify(F2 @ A3)

        A4 = A.subs([(d, 0), (theta, th4), (a, 0), (alpha, np.deg2rad(-90))])
        F4 = sp.simplify(F3 @ A4)

        A5 = A.subs([(d, l3), (theta, th5), (a, 0), (alpha, np.deg2rad(90))])
        F5 = sp.simplify(F4 @ A5)

        A6 = A.subs([(d, 0), (theta, th6), (a, 0), (alpha, np.deg2rad(-90))])
        F6 = sp.simplify(F5 @ A6)

        A7 = A.subs([(d, l4), (theta, th7), (a, 0), (alpha, 0)])
        F7 = sp.simplify(F6 @ A7)

        print(sp.latex(sp.simplify(F7)))
        print(sp.pretty(sp.simplify(F7)))

    # Fazendo o calculo numerico, devido a eficiência
    L1, L2, L3, L4 = 1, 1, 1, 1 # links fixos
    TH1, TH2, TH3 = np.deg2rad(0), np.deg2rad(0), np.deg2rad(0)
    TH4, TH5, TH6, TH7 = np.deg2rad(0), np.deg2rad(0), np.deg2rad(0), np.deg2rad(0)

    f0 = np.eye(4)
    f1 = f0 @ numeric_DH(L1, TH1, 0, np.deg2rad(90))
    f2 = f1 @ numeric_DH(0, TH2, 0, np.deg2rad(-90))
    f3 = f2 @ numeric_DH(L2, TH3, 0, np.deg2rad(90))
    f4 = f3 @ numeric_DH(0, TH4, 0, np.deg2rad(-90))
    f5 = f4 @ numeric_DH(L3, TH5, 0, np.deg2rad(90))
    f6 = f5 @ numeric_DH(0, TH6, 0, np.deg2rad(-90))
    f7 = f6 @ numeric_DH(L4, TH7, 0, 0)

    frames = [f0, f1, f2, f3, f4, f5, f6, f7]

    # Plotando o robô na posicao zero
    plt.figure(1)
    fig = plt.axes(projection='3d')

    plot_robot(fig, frames, origin=True)

    #Frame arbitrario
    TH1, TH2, TH3 = np.deg2rad(45), np.deg2rad(-45), np.deg2rad(-45) # angulos das juntas
    TH4, TH5, TH6, TH7 = np.deg2rad(45), np.deg2rad(-45), np.deg2rad(-45), np.deg2rad(45) # angulos das juntas

 
    f0 = np.eye(4)
    f1 = f0 @ numeric_DH(L1, TH1, 0, np.deg2rad(90))
    f2 = f1 @ numeric_DH(0, TH2, 0, np.deg2rad(-90))
    f3 = f2 @ numeric_DH(L2, TH3, 0, np.deg2rad(90))
    f4 = f3 @ numeric_DH(0, TH4, 0, np.deg2rad(-90))
    f5 = f4 @ numeric_DH(L3, TH5, 0, np.deg2rad(90))
    f6 = f5 @ numeric_DH(0, TH6, 0, np.deg2rad(-90))
    f7 = f6 @ numeric_DH(L4, TH7, 0, 0)

    frames = [f0, f1, f2, f3, f4, f5, f6, f7]

    # Plotando o robô na posicao zero
    plt.figure(2)
    fig2 = plt.axes(projection='3d')

    plot_robot(fig2, frames, origin=True, show=True)