def balance_brackets(expr):
    open_needed = 0
    close_needed = 0
    
    for char in expr:
        if char == '(':
            open_needed += 1
        elif char == ')':
            if open_needed > 0:
                open_needed -= 1
            else:
                close_needed += 1
    
    balanced_expr = '(' * close_needed + expr + ')' * open_needed
    
    return balanced_expr

input_expr = "(a+b(c)"
output_expr = balance_brackets(input_expr)
print(f"Input: {input_expr}")
print(f"Balanced Output: {output_expr}")
