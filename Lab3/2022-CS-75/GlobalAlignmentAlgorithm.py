import numpy as np

def sequence_alignment(S, T, match_score=1, mismatch_penalty=-1, gap_penalty=-2):
    n, m = len(S), len(T)
    
    # Initialize the scoring matrix
    matrix = np.zeros((n+1, m+1), dtype=int)
    for i in range(1, n+1):
        matrix[i][0] = gap_penalty * i
    for j in range(1, m+1):
        matrix[0][j] = gap_penalty * j

    # Fill the matrix
    for i in range(1, n+1):
        for j in range(1, m+1):
            match = matrix[i-1][j-1] + (match_score if S[i-1] == T[j-1] else mismatch_penalty)
            delete = matrix[i-1][j] + gap_penalty
            insert = matrix[i][j-1] + gap_penalty
            matrix[i][j] = max(match, delete, insert)

    # Traceback
    alignment_S, alignment_T = [], []
    i, j = n, m
    while i > 0 or j > 0:
        if i > 0 and j > 0 and matrix[i][j] == matrix[i-1][j-1] + (match_score if S[i-1] == T[j-1] else mismatch_penalty):
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

    # Output result
    print("Optimal Alignment:")
    print(''.join(reversed(alignment_S)))
    print(''.join(reversed(alignment_T)))
    print(f"Alignment Score: {matrix[-1, -1]}")

# Test with sequences
S = "ATGCT"
T = "AGCT"
sequence_alignment(S, T)
