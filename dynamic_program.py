import numpy as np

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

V = np.zeros((1, 5)) #arbitrarily initialized state value function

theta = 1.2 #arbitrarily chosen small positive number as a stopping condition
gamma = 0.95 #discount factor
delta = 0

while(True):
    delta = 0
    for s in range(np.size(V, 1)):
        v = V[0][s]
        sum_ao = 0
        sum_a1 = 0

        s_prime = np.nonzero(p_s_a0[s])
        for ii in s_prime[0]:
            sum_ao += sum_ao + p_s_a0[s][ii]*(r[s][0] + gamma*V[0][ii])

        s_prime = np.nonzero(p_s_a1[s])
        for ii in s_prime[0]:
            sum_a1 += sum_a1 + p_s_a1[s][ii]*(r[s][1] + gamma*V[0][ii])

        V[0][s] = max(sum_ao, sum_a1)
        delta = max(delta, abs(v - V[0][s]))
    if(delta < theta):
        break

print(V)

q = np.zeros((5,2))

for s in range(np.size(V, 1)):
    s_prime = np.nonzero(p_s_a0[s])
    for ii in s_prime[0]:
        q[s][0] += q[s][0] + p_s_a0[s][ii]*(r[s][0] + gamma*V[0][ii]);

    s_prime = np.nonzero(p_s_a1[s])
    for ii in s_prime[0]:
        q[s][1] += q[s][1] + p_s_a1[s][ii]*(r[s][1] + gamma*V[0][ii]);

print(q)
