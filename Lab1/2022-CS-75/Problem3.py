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
