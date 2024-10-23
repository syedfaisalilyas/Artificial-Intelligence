import numpy as np

match_score = 1
mismatch_penalty = -1
gap_penalty = -2


def initialize_matrix(n, m):
    matrix = np.zeros((n+1, m+1), dtype=int)
    
    for i in range(1, n+1):
        matrix[i][0] = gap_penalty * i
    for j in range(1, m+1):
        matrix[0][j] = gap_penalty * j
    
    return matrix

def compute_alignment_matrix(S, T):
    n, m = len(S), len(T)
    
    matrix = initialize_matrix(n, m)
    
    for i in range(1, n+1):
        for j in range(1, m+1):
            if S[i-1] == T[j-1]:
                match = matrix[i-1][j-1] + match_score  # match
            else:
                match = matrix[i-1][j-1] + mismatch_penalty  # mismatch
            
            delete = matrix[i-1][j] + gap_penalty  # gap in T
            insert = matrix[i][j-1] + gap_penalty  # gap in S
            
            matrix[i][j] = max(match, delete, insert)  
    
    return matrix

def traceback(matrix, S, T):
    alignment_S = []
    alignment_T = []
    
    i, j = len(S), len(T)
    
    while i > 0 or j > 0:
        current_score = matrix[i][j]
        
        if i > 0 and j > 0 and (S[i-1] == T[j-1] or matrix[i][j] == matrix[i-1][j-1] + mismatch_penalty):
            alignment_S.append(S[i-1])
            alignment_T.append(T[j-1])
            i -= 1
            j -= 1
        elif i > 0 and matrix[i][j] == matrix[i-1][j] + gap_penalty:
            alignment_S.append(S[i-1])
            alignment_T.append('-')
            i -= 1
        else:
            alignment_S.append('-')
            alignment_T.append(T[j-1])
            j -= 1
    
    return ''.join(reversed(alignment_S)), ''.join(reversed(alignment_T))

def sequence_alignment(S, T):
    alignment_matrix = compute_alignment_matrix(S, T)
    
    alignment_S, alignment_T = traceback(alignment_matrix, S, T)
    
    print("Optimal Alignment:")
    print(alignment_S)
    print(alignment_T)
    print(f"Alignment Score: {alignment_matrix[-1, -1]}")

S = "AGCT"
T = "GCTA"

sequence_alignment(S, T)
