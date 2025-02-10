from model_tools import *
from auxiliar_plots import *
import matplotlib.pyplot as plt
import sympy as sp

# Codigo relativo a testes das funcoes nao e necessario para o entendimento do codigo
# nem mesmo sua referencia no relatorio


if __name__ == '__main__':
    # Create a model

    # Robô ARTICULADO 4DOF RRRP:
    # |=====================================|
    # | Ai | d      | theta   | a   | alpha |
    # |----|--------|---------|-----|-------|
    # | 1  | l1     | th1*    | 0   | -90   |
    # | 2  | 0      | th2*    | l2  | 0     |
    # | 3  | 0      | th3*    | l3  | 0     |
    # |=====================================|

    
    # Joint variables
    th1, th2, th3, l0, l1, l2, l3, l4 = sp.symbols('th1 th2 th3 l0 l1 l2 l3 l4', real=True)

    F0 = np.eye(4)

    A1 = A.subs([(d, l1), (theta, th1), (a, 0), (alpha, np.deg2rad(-90))])
    F1 = sp.simplify(F0 @ A1)

    A2 = A.subs([(d, 0), (theta, th2), (a, l2), (alpha, 0)])
    F2 = sp.simplify(F1 @ A2)

    A3 = A.subs([(d, 0), (theta, th3), (a, l3), (alpha, 0)])
    F3 = sp.simplify(F2 @ A3)

    # Replace joint and link parameters with numerical values
    L0, L1, L2, L3, L4 = 0, 3, 1, 1, 1
    TH1, TH2, TH3 = np.deg2rad(0), np.deg2rad(0), np.deg2rad(0)

    f0 = F0
    f1 = F1.subs([(l1, L1), (th1, TH1), (l2, L2), (th2, TH2), (l3, L3), (th3, TH3), (l4, L4)])
    f2 = F2.subs([(l1, L1), (th1, TH1), (l2, L2), (th2, TH2), (l3, L3), (th3, TH3), (l4, L4)])
    f3 = F3.subs([(l1, L1), (th1, TH1), (l2, L2), (th2, TH2), (l3, L3), (th3, TH3), (l4, L4)])

    # Convert symbolic matrices to numerical matrices
    f0 = np.array(f0, dtype=float)
    f1 = np.array(f1.evalf(), dtype=float)
    f2 = np.array(f2.evalf(), dtype=float)
    f3 = np.array(f3.evalf(), dtype=float)

    #numertical execution time
    # # Joint variables
    # f0_n = np.eye(4)
    # f1_n = f0_n @ numeric_DH(L1, TH1, 0 , np.deg2rad(-90))
    # f2_n = f1_n @ numeric_DH(0 , TH2, L2, 0)
    # f3_n = f2_n @ numeric_DH(0 , TH3, L3, 0)


    plt.figure()
    fig = plt.axes(projection='3d')

    # Plot frames
    plot_frame_a(fig, f0, '0')
    plot_frame_a(fig, f1, '1')
    plot_frame_a(fig, f2, '2')
    plot_frame_a(fig, f3, '3')

    # Plot transitions
    plot_transicao_ab(fig, f0, f1)
    plot_transicao_ab(fig, f1, f2)
    plot_transicao_ab(fig, f2, f3, show=True)
