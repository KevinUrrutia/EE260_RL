import numpy as np

r = np.array([[0, 0.2],
             [0, 0.2],
             [0, 0.2],
             [0, 0.2],
             [1, 0.2]])

q = np.zeros((5, 2))

pi = np.zeros((5, 2))

gamma = 0.95
epsilon = 0.2

returns = []

while(True):
    for s in range(np.size(pi, 0)):
        G_a0 = (r[s][0]) / (1 - gamma)
        G_a1 = (r[s][1]) / (1 - gamma)

        q[s][0] = G_a0
        q[s][1] = G_a1

        A_star = np.argmax(q[s])

        for ii in range(np.size(pi, 1)):
            if(ii == A_star):
                pi[s][ii] = epsilon / 2
            else:
                pi[s][ii] = 1 - epsilon + (epsilon / 2)
print(q)
