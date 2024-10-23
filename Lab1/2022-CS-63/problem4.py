

# Problem 4: Simplifying Nested Expressions
def reduce_expression(expression):
    if isinstance(expression, (int, str)):
        return expression
    elif isinstance(expression, list):
        operation = expression[0]
        if operation == '+':
            terms = []
            for part in expression[1:]:
                reduced = reduce_expression(part)
                if isinstance(reduced, list) and reduced[0] == '+':
                    terms.extend(reduced[1:])
                else:
                    terms.append(reduced)
            return ['+'] + terms
        elif operation == '*':
            left = reduce_expression(expression[1])
            right = reduce_expression(expression[2])
            if isinstance(left, list) and left[0] == '+':
                return reduce_expression(['+'] + [['*', term, right] for term in left[1:]])
            elif isinstance(right, list) and right[0] == '+':
                return reduce_expression(['+'] + [['*', left, term] for term in right[1:]])
            else:
                return ['*', left, right]

expr_example = ['*', 2, ['+', 'x', 1], ['+', 'y', 3]]
simplified = reduce_expression(expr_example)
print(f"Simplified expression: {simplified}")
