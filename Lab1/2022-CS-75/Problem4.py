
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
