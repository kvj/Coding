""" Node is defined as
class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
"""

def check_binary_search_tree_(root):
    def check_place(r, node):
        if r == node:
            return True
        if r.data == node.data:
            return False # Duplicate
        if r.data > node.data:
            if r.left:
                return check_place(r.left, node)
            else:
                return False # Invalid
        else:
            if r.right:
                return check_place(r.right, node)
            else:
                return False # Invalid
    def check_node(r):
        if not r:
            return False
        values.append(r.data)
        if r.left and r.left.data >= r.data:
            return False
        if r.right and r.right.data <= r.data:
            return False
        if r.left and not check_node(r.left):
            return False
        if r.right and not check_node(r.right):
            return False
        if not check_place(root, r):
            return False
        return True
    return check_node(root)
