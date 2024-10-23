
# Problem 2: 
def calculate_depth(expression):
    if not isinstance(expression, tuple):
        return 0
    return 1 + max(calculate_depth(sub_expr) for sub_expr in expression)

example_tuple = ((1, 2), 3, (4, (5, 6)), 7)
depth_value = calculate_depth(example_tuple)
print(f"The depth of the tuple is: {depth_value}")


