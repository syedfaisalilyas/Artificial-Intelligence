# Problem 1a: Factorial Function
def compute_factorial(n):
    if n < 0:
        return "Invalid input"
    elif n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(2, n+1):
            result *= i
        return result

factorial_result = compute_factorial(5)
if factorial_result == "Invalid input":
    print(factorial_result)
else:
    print(f"The factorial is: {factorial_result}")


# Problem 1b: Cube Function
def calculate_cube(num):
    return num ** 3

cube_result = calculate_cube(2)
print(f"The cube of 2 is: {cube_result}")


# Problem 1c: Find Alphabetically Last Word
def last_word_in_order(sentence):
    words = sentence.split()
    return max(words)

sentence_example = "What is the last word in this sentence?"
alphabetically_last_word = last_word_in_order(sentence_example)
print(f"The last word alphabetically is: {alphabetically_last_word}")


# Problem 1d: Count Pattern in List
def pattern_counter(pattern, sequence):
    pattern_size = len(pattern)
    occurrences = 0
    for i in range(len(sequence) - pattern_size + 1):
        if tuple(sequence[i:i + pattern_size]) == pattern:
            occurrences += 1
    return occurrences

result1 = pattern_counter(('a', 'b'), ['a', 'b', 'c', 'e', 'b', 'a', 'b', 'f'])
result2 = pattern_counter(('a', 'b', 'a'), ['g', 'a', 'b', 'a', 'b', 'a', 'b', 'a'])
print(f"Pattern 1 occurrences: {result1}")
print(f"Pattern 2 occurrences: {result2}")

