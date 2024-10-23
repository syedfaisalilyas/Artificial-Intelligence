# Problem 1 a
def factorial(n):
    if n == 0 or n == 1:
        return 1
    elif n<0:
        return -1
    else:
        return n * factorial(n-1)
answer=factorial(5)
if answer==-1:
    print("Input must not be negative")
else:
    print(answer)


# Problem 1 b
def cube(n):
    if(n==0):
        return 0
    else:
        return n*n*n
print(cube(2))

# Problem1 c
def findAlphabeticallyLastWord(sentence):
    sentence = sentence.split()
    sentence.sort()
    last_word = sentence[-1]
    return last_word
sentence = "What is the last word in this sentence?"
result = findAlphabeticallyLastWord(sentence)
print(result) 

# Problem1 d
def count_pattern(pattern, lst):
    pattern_len = len(pattern)
    count = 0
    for i in range(len(lst) - pattern_len + 1):
        if tuple(lst[i:i + pattern_len]) == pattern:
            count += 1
    return count
result1 = count_pattern(('a', 'b'), ('a', 'b', 'c', 'e', 'b', 'a', 'b', 'f'))
result2 = count_pattern(('a', 'b', 'a'), ('g', 'a', 'b', 'a', 'b', 'a', 'b', 'a'))
print(result1)  
print(result2) 
 
