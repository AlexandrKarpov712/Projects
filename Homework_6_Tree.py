import mymodule as m

"""Creating a tree"""
tree = m.TreeNode(1)
tree.left = m.TreeNode(2)
tree.right = m.TreeNode(3)
tree.left.left = m.TreeNode(4)
tree.left.right = m.TreeNode(5)


def pre_order(node):
    """Pre-order tree traversal.

    Input arguments: root node.
    Output: print from parent to all of its descendants.
    """
    if node:
        print(node.value)
        pre_order(node.left)
        pre_order(node.right)

print("Прямой обход дерева: ")
pre_order(tree)

