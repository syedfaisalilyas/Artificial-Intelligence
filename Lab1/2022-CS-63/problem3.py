# Problem 3: Tree Reference
def access_tree_element(tree_structure, position):
    element = tree_structure
    for index in position:
        element = element[index]
    return element

example_tree = (((1, 2), 3), (4, (5, 6)), 7, (8, 9, 10))
print(access_tree_element(example_tree, [3, 1]))  
print(access_tree_element(example_tree, [1, 1, 1]))  
print(access_tree_element(example_tree, [0]))
