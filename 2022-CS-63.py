import numpy as np

n_rows, n_cols = 4, 4 
n_states = n_rows * n_cols  
UP, DOWN, LEFT, RIGHT = 0, 1, 2, 3 
actions = [UP, DOWN, LEFT, RIGHT]  

# _______ INITIALIZE TRANSITION AND REWARD MATRICES _______
P = np.zeros((n_states, len(actions), n_states)) 
R = np.zeros((n_states, len(actions)))        
def to_state(row, col):
    # _______ CONVERT GRID COORDINATES TO STATE NUMBER _______
    return row * n_cols + col  

def from_state(state):
    # _______ CONVERT STATE NUMBER BACK TO GRID COORDINATES _______
    return divmod(state, n_cols) 

# _______ DEFINE REWARDS FOR SPECIFIC POSITIONS _______
rewards = {
    (2, 1): -50,  # _______ -50 REWARD AT POSITION (2, 1) _______
    (1, 4): -5,   # _______ -5 REWARD AT POSITION (1, 4) _______
    (4, 4): 70    # _______ 70 REWARD AT GOAL POSITION (4, 4) _______
}

# _______ DEFINE TERMINAL STATES _______
terminal_states = [to_state(2, 3), to_state(3, 3)] 

# _______ DEFINE TRANSITIONS _______
for row in range(n_rows):
    for col in range(n_cols):
        s = to_state(row, col)  # _______ GET THE CURRENT STATE _______
        
        if s in terminal_states:  # _______ SKIP TERMINAL STATES _______
            continue  # _______ NO TRANSITIONS FROM TERMINAL STATES _______

        # _______ MOVING UP _______
        if row > 0:
            next_s = to_state(row - 1, col)  # _______ MOVE TO THE STATE ABOVE _______
        else:
            next_s = s  
        P[s, UP, next_s] = 1  

        # _______ MOVING DOWN _______
        if row < n_rows - 1:
            next_s = to_state(row + 1, col)  
        else:
            next_s = s  
        P[s, DOWN, next_s] = 1  # _______ SET TRANSITION PROBABILITY TO 1 _______

        # _______ MOVING LEFT _______
        if col > 0:
            next_s = to_state(row, col - 1)  # _______ MOVE TO THE LEFT STATE _______
        else:
            next_s = s  
        P[s, LEFT, next_s] = 1 

        # _______ MOVING RIGHT _______
        if col < n_cols - 1:
            next_s = to_state(row, col + 1)  # _______ MOVE TO THE RIGHT STATE _______
        else:
            next_s = s 
        P[s, RIGHT, next_s] = 1  # _______ SET TRANSITION PROBABILITY TO 1 _______

        # _______ ASSIGN REWARDS BASED ON POSITION _______
        for a in actions:  
            r, c = from_state(s) 
            R[s, a] = rewards.get((r + 1, c + 1), 0) 

# _______ VALUE ITERATION FUNCTION _______
def value_iteration(P, R, gamma=0.9, theta=0.0001):
    # _______ ALGORITHM TO COMPUTE THE OPTIMAL POLICY _______
    V = np.zeros(n_states)  
    policy = np.zeros(n_states, dtype=int)  

    while True:  
        delta = 0  
        for s in range(n_states): 
            if s in terminal_states:  
                continue  

            v = V[s] 
            V[s] = max([sum([P[s, a, s_prime] * (R[s, a] + gamma * V[s_prime]) 
                             for s_prime in range(n_states)]) for a in actions])
            delta = max(delta, abs(v - V[s])) 

        if delta < theta:  
            break  
    for s in range(n_states):
        if s in terminal_states:
            continue

        action_values = []
        for a in actions:
            action_value = sum([P[s, a, s_prime] * (R[s, a] + gamma * V[s_prime])
                                for s_prime in range(n_states)])
            action_values.append(action_value)
        policy[s] = np.argmax(action_values)

    return policy, V

# _______ SOLVE MDP _______
policy, value_function = value_iteration(P, R)

# _______ DISPLAY RESULTS _______
def display_policy(policy):
    action_symbols = {UP: '↑', DOWN: '↓', LEFT: '←', RIGHT: '→'}
    grid_policy = []
    for row in range(n_rows):
        grid_row = []
        for col in range(n_cols):
            state = to_state(row, col)
            if state in terminal_states:
                grid_row.append('END')
            else:
                grid_row.append(action_symbols[policy[state]])
        grid_policy.append(grid_row)
    return grid_policy
optimal_policy = display_policy(policy)
for row in optimal_policy:
    print(row)

print("\nState Values:")
value_grid = value_function.reshape((n_rows, n_cols))
print(value_grid)
