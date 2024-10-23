# Problem2 a
def depth(expr):
    if not isinstance(expr, tuple):
        return 0
    else:
        return 1 + max(depth(sub_expr) for sub_expr in expr)

