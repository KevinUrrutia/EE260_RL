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

Q = np.random.rand(5, 2)

gamma = 0.95
theta = 0.001
delta = 0
alpha = 0.01
epsilon = 0.1

returns = []

while(True):
    delta = 0
    for s in range(np.size(Q, 1)):
        A_star = selectAction(Q, s, epsilon) #select A using an epsilon greedy policy
        q = Q[s][A_star]
        R = r[A_star][s]
        if(A_star == 0):
            S_prime = np.argmax(p_s_a0[s])
        else:
            S_prime = np.argmax(p_s_a1[s])

        Q[s][A_star] = Q[s][A_star] + alpha*(R + gamma*max(Q[s]) - Q[s][A_star])

        delta = max(delta, abs(q - Q[s][A_star]))
        print(delta)
    if(delta < theta):
        break

print(Q)
