import numpy as np
import random as rnd

def selectAction(Q, s, epsilon):
    if(rnd.uniform(0, 1) < epsilon):
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

gamma = 0.95
theta = 1e-5
delta = 0
alpha = 0.1
epsilon = 0.1
s = 0


while(True):
    delta = 0
    A_star = selectAction(Q, s, epsilon) #select A using an epsilon greedy policy
    q = Q[s][A_star]
    R = r[s][A_star]
    if(A_star == 0):
        S_prime = np.argmax(p_s_a0[s])
    else:
        S_prime = np.argmax(p_s_a1[s])


    Q[s][A_star] = Q[s][A_star] + alpha*(R + gamma*max(Q[S_prime]) - Q[s][A_star])

    delta = max(delta, abs(q - Q[s][A_star]))
    # print(abs(q - Q[s][A_star]))

    s = S_prime
    # if(delta < theta):
    #     break

    print(Q)
