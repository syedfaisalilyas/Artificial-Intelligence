counter = 0  # Global counter to count recursive calls

# Recursive function
def quiz(n):
    global counter
    if n == 0 or n == 1:
        return n
    else:
        counter += 1  # Increment counter for every recursive call
        return ((quiz(n - 1) - quiz(n - 2)) * quiz(n - 1))


# Dynamic programming function
def dp(n):
    # Initialize a list of size n+1 to store results
    dyp = [0] * (n + 1)

    # Base cases
    dyp[0] = 0
    if n > 0:
        dyp[1] = 1

    # Fill the dyp array for all numbers from 2 to n
    for i in range(2, n + 1):
        dyp[i] = (dyp[i - 1] - dyp[i - 2]) * dyp[i - 1]

    return dyp[n]


# Example usage
print("Result from dp function for n=3:", dp(3))  # Output will depend on your logic
print("Counter from quiz function:", counter)  # Counter for recursive calls
