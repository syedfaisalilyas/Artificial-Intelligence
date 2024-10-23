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
print(cube(8))

# Problem 1 c
def findAlphabeticallyLastWord(sentence):
    sentence = sentence.split()
    sentence.sort()
    last_word = sentence[-1]
    return last_word
sentence = "What is the last word in this sentence?"
result = findAlphabeticallyLastWord(sentence)
print(result) 

# Problem 1 d
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
 
# Problem 2 a
def depth(expr):
    if not isinstance(expr, tuple):
        return 0
    else:
        return 1 + max(depth(sub_expr) for sub_expr in expr)

# Problem 3 
def tree_ref(tree, index):
    result = tree
    for i in index:
        result = result[i]
    return result
tree = (((1, 2), 3), (4, (5, 6)), 7, (8, 9, 10))
print(tree_ref(tree, [3, 1])) 
print(tree_ref(tree, [1, 1, 1]))  
print(tree_ref(tree, [0]))  

# Problem 4
def simplify(expr):
    if isinstance(expr, int): 
        return expr
    elif isinstance(expr, str):
        return expr
    elif isinstance(expr, list):  
        op = expr[0]  
        if op == '+':
            result = []
            for sub_expr in expr[1:]:
                sub_simplified = simplify(sub_expr)
                if isinstance(sub_simplified, list) and sub_simplified[0] == '+':
                    result.extend(sub_simplified[1:])
                else:
                    result.append(sub_simplified)
            return ['+'] + result
        elif op == '*':
            left = simplify(expr[1])
            right = simplify(expr[2])
            if isinstance(left, list) and left[0] == '+':
                return simplify(['+'] + [['*', term, right] for term in left[1:]])
            elif isinstance(right, list) and right[0] == '+':
                return simplify(['+'] + [['*', left, term] for term in right[1:]])
            else:
                return ['*', left, right]

expr = ['*', 2, ['+', 'x', 1], ['+', 'y', 3]]
simplified_expr = simplify(expr)
print(simplified_expr)
