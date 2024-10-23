def balance_brackets(expr):
    open_needed = 0  
    close_needed = 0  

    for char in expr:
        if char == '(':
            close_needed += 1
        elif char == ')':
            if close_needed > 0:
                close_needed -= 1
            else:
                open_needed += 1

    balanced_expr = '(' * open_needed + expr + ')' * close_needed
    return balanced_expr
input_expr = ")a+b((c"
balanced_expr = balance_brackets(input_expr)
print(f"Balanced expression: {balanced_expr}")
