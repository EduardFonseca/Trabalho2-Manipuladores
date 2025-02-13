# import sympy as sp

# def symbolic_DH(d, theta, a, alpha):
#     """Returns a symbolic DH transformation matrix"""
#     return sp.Matrix([
#         [sp.cos(theta), -sp.sin(theta) * sp.cos(alpha),  sp.sin(theta) * sp.sin(alpha), a * sp.cos(theta)],
#         [sp.sin(theta),  sp.cos(theta) * sp.cos(alpha), -sp.cos(theta) * sp.sin(alpha), a * sp.sin(theta)],
#         [0,             sp.sin(alpha),                  sp.cos(alpha),                  d],
#         [0,             0,                               0,                               1]
#     ])  # Using optimized DH matrix function


# # Define symbolic joint variables
# th1, th2, d3 = sp.symbols('th1 th2 d3', real=True)
# l1, l2 = sp.symbols('l1 l2', real=True)

# # Define DH parameters for Planar RRP robot
# # (d, theta, a, alpha)
# dh_params = [
#     (0, th1, l1, 0),
#     (0, sp.pi/2 + th2, 0, sp.pi/2),
#     (l2 + d3, 0, 0, 0)
# ]


# # Compute transformation matrices
# F = sp.eye(4)
# for params in dh_params:
#     F = F @ symbolic_DH(*params)  # Compute each transformation iteratively

# # Apply targeted simplifications
# F_simplified = sp.trigsimp(F)
# F_simplified = sp.nsimplify(F_simplified, tolerance=1e-10)

# # # Print results
# # print("LaTeX Output:")
# # print(sp.latex(F_simplified))
# print("Pretty Output:")
# print(sp.pretty(F_simplified))
import sympy as sp
from model_tools import *

print(sp.pretty(A))