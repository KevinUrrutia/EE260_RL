import numpy as np
import random as rnd

def selectAction(Q, s, epsilon):
    p_a = rnd.random();
    if(p_a < epsilon):
        A = rnd.randint(0, 1)
    else:
        A = np.argmax(Q[s])

    return A

r = np.array([[0, 0.2],
             [0, 0.2],
             [0, 0.2],
             [0, 0.2],
             [1, 0.2]])

p_s_a0 = np.array([[0, 0.8, 0.2, 0, 0],
                   [0, 0, 0.8, 0.2, 0],
                   [0, 0, 0.2, 0.8, 0],
                   [0, 0, 0,   0,   1],
                   [0, 0, 0,   0,   1]])

p_s_a1 = np.array([[0.9, 0.1, 0, 0, 0],
                   [0.9, 0.1, 0, 0, 0],
                   [0.9, 0, 0.1, 0, 0],
                   [0.9, 0, 0.1, 0, 0],
                   [0.9, 0, 0.1, 0, 0]])

Q = np.zeros((5, 2))
V = np.zeros((1, 5))

gamma = 0.95
theta = 1.2
delta = 0
epsilon = 0.1

returns = []

while(True):
    delta = 0
    for s in range(np.size(V, 1)):
        A_star = selectAction(Q, s, epsilon)
        print(A_star)
        break
    break
