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
Q = np.zeros((5, 2))

theta = 1e-5 #arbitrarily chosen small positive number as a stopping condition
gamma = 0.95 #discount factor
delta = 0
s = 0

while(True):
    delta = 0
    for s in range(np.size(V, 1)):
        next_states = np.nonzero(p_s_a0[s])
        sum_ao = 0
        for s_prime in next_states[0]:
            sum_ao = p_s_a0[s][s_prime] + (r[s][0] + gamma*max(Q[s_prime]))

        sum_a1 = 0
        next_states = np.nonzero(p_s_a1[s])
        for s_prime in next_states[0]:
            sum_a1 = p_s_a1[s][s_prime] + (r[s][1] + gamma*max(Q[s_prime]))

        Q[s][0] = sum_ao
        Q[s][1] = sum_a1
        print(Q/2)
        # delta = max(delta, abs(q - Q[s][A_star]))

    # if(delta < theta):
    #     break
