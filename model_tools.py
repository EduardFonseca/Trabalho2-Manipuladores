import sympy as sp
import numpy as np

# global symbolic variables\
d, theta, a, alpha = sp.symbols('d theta a alpha', real=True)

TX = sp.Matrix([[1, 0, 0, a],
                [0, 1, 0, 0],
                [0, 0, 1, 0],
                [0, 0, 0, 1]])

TZ = sp.Matrix([[1, 0, 0, 0],
                [0, 1, 0, 0],
                [0, 0, 1, d],
                [0, 0, 0, 1]])

RX = sp.Matrix([[1,     0        ,      0        ,0],
                [0, sp.cos(alpha), -sp.sin(alpha),0],
                [0, sp.sin(alpha),  sp.cos(alpha),0],
                [0,     0        ,      0        ,1]])

RZ = sp.Matrix([[sp.cos(theta), -sp.sin(theta), 0, 0],
                [sp.sin(theta),  sp.cos(theta), 0, 0],
                [    0        ,      0        , 1, 0],
                [    0        ,      0        , 0, 1]])

A = sp.simplify(TZ @ RZ @ TX @ RX )


def numeric_DH(d,theta,a,alpha):
    '''
    Create a Denavit-Hartenberg matrix using numerical values
    Parameters:
        d: float
        theta: float
        a: float
        alpha: float
    Returns:
        np.array: 4x4 matrix
    '''
    Tx = np.array([[1, 0, 0, a],
                   [0,1,0,0],
                   [0,0,1,0],
                   [0,0,0,1]])
    Rx = np.array([[1,     0        ,      0        ,0],
                   [0, np.cos(alpha), -np.sin(alpha),0],
                   [0, np.sin(alpha),  np.cos(alpha),0],
                   [0,     0        ,      0        ,1]])
    Tz = np.array([[1, 0, 0, 0],
                   [0, 1, 0, 0],
                   [0, 0, 1, d],
                   [0, 0, 0, 1]])
    Rz = np.array([[np.cos(theta), -np.sin(theta), 0, 0],
                   [np.sin(theta),  np.cos(theta), 0, 0],
                   [    0        ,      0        , 1, 0],
                   [    0        ,      0        , 0, 1]])
    
    return Tz @ Rz @ Tx @ Rx

__all__ = ["d", "theta", "a", "alpha", "TX", "TZ", "RX", "RZ", "A", "numeric_DH"]



