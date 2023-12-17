import random

class Node:
    def __init__(self, key):
        self.key = key
        self.left = self.right = None

def create_random_tree(n):
    import random
    nums = random.sample(range(101), n)
    root = Node(nums[0])
    for num in nums[1:]:
        insert(root, num)
    return root

def insert(root, key):
    if root is None:
        return Node(key)
    if key < root.key:
        root.left = insert(root.left, key)
    else:
        root.right = insert(root.right, key)
    return root

def flatten_to_list(root):
    result = []
    inorder_traversal(root, result)
    return result

def inorder_traversal(root, result):
    if root:
        inorder_traversal(root.left, result)
        result.append(root.key)
        inorder_traversal(root.right, result)

def create_dsw_tree(root):
    nodes = flatten_to_list(root)
    return dsw_algorithm(nodes, 0, len(nodes))

def dsw_algorithm(nodes, i, n):
    if n <= 1:
        return None
    m = 2**((n+1).bit_length()-1) - 1
    root = Node(nodes[i + m//2])
    root.left = dsw_algorithm(nodes, i, m//2)
    root.right = dsw_algorithm(nodes, i + m + 1, n - m - 1)
    return root


random_tree = create_random_tree(100)


balanced_tree = create_dsw_tree(random_tree)


def add_numbers_to_tree(root, numbers):
    for number in numbers:
        root = insert(root, number)
    return root


additional_numbers = random.sample(range(101, 1000), 20)


tree_with_additional_numbers = add_numbers_to_tree(balanced_tree, additional_numbers)


final_balanced_tree = create_dsw_tree(tree_with_additional_numbers)


print("Árvore Original:")
print(flatten_to_list(random_tree))


print("Árvore Balanceada com 20 Números Adicionados:")
print(flatten_to_list(tree_with_additional_numbers))


print("Nova Árvore Balanceada com Algoritmo DSW:")
print(flatten_to_list(final_balanced_tree))
