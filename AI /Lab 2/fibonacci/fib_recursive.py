def fibonacci_recursive(n):
    if n <= 1:
        return n
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

n = 10
print(f"Fibonacci (Recursive) at position {n}: {fibonacci_recursive(n)}")
