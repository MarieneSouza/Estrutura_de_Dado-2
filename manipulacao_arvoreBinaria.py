import random

class Node:
    def __init__(self, key):
        self.key = key
        self.left = self.right = None

def insert(root, key):
    if root is None:
        return Node(key)
    if key < root.key:
        root.left = insert(root.left, key)
    else:
        root.right = insert(root.right, key)
    return root

def preorder_traversal(root):
    if root:
        print(root.key, end=' ')
        preorder_traversal(root.left)
        preorder_traversal(root.right)

def inorder_traversal(root):
    if root:
        inorder_traversal(root.left)
        print(root.key, end=' ')
        inorder_traversal(root.right)

def postorder_traversal(root):
    if root:
        postorder_traversal(root.left)
        postorder_traversal(root.right)
        print(root.key, end=' ')

def level_order_traversal(root):
    if not root:
        return
    queue = [root]
    while queue:
        node = queue.pop(0)
        print(node.key, end=' ')
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)


def remove_elements(root, elements):
    for element in elements:
        root = remove(root, element)
    return root

def remove(root, key):
    if root is None:
        return root
    if key < root.key:
        root.left = remove(root.left, key)
    elif key > root.key:
        root.right = remove(root.right, key)
    else:
        if root.left is None:
            return root.right
        elif root.right is None:
            return root.left
        root.key = min_value_node(root.right).key
        root.right = remove(root.right, root.key)
    return root

def min_value_node(node):
    current = node
    while current.left is not None:
        current = current.left
    return current

random_numbers = random.sample(range(101), 20)

root = None
for number in random_numbers:
    root = insert(root, number)

print("Sequência de Pré-Ordem:")
preorder_traversal(root)
print("\nSequência de In-Ordem:")
inorder_traversal(root)
print("\nSequência de Pós-Ordem:")
postorder_traversal(root)
print("\nSequência em Nível:")
level_order_traversal(root)


elements_to_remove = random.sample(random_numbers, 5)
root = remove_elements(root, elements_to_remove)


print("\n\nApós Remover 5 Elementos:")
print("Sequência de Pré-Ordem:")
preorder_traversal(root)
print("\nSequência de In-Ordem:")
inorder_traversal(root)
print("\nSequência de Pós-Ordem:")
postorder_traversal(root)
print("\nSequência em Nível:")
level_order_traversal(root)
