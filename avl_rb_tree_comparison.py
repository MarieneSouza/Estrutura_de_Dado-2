
from sortedcontainers import SortedDict
from sortedcontainers import SortedDict
from sortedcontainers import SortedDict
import time
import random

# Leitura dos dados do arquivo
with open("4P/Fernando/estruturaDeDados2/dados100_mil.txt", "r") as file:
    lines = file.readlines()

# Extrair números das linhas
array_from_file = []
for line in lines:
    numbers = [int(num) for num in line.strip('[]').split(',')]
    array_from_file.extend(numbers)

# Preenchimento da árvore AVL (usando SortedDict como substituto)
avl_tree = SortedDict()
start_time_avl = time.time()
for num in array_from_file:
    avl_tree[num] = None
end_time_avl = time.time()
insertion_time_avl = end_time_avl - start_time_avl

# Preenchimento da árvore Rubro-Negra (usando SortedDict como substituto)
rb_tree = SortedDict()
start_time_rb = time.time()
for num in array_from_file:
    rb_tree[num] = None
end_time_rb = time.time()
insertion_time_rb = end_time_rb - start_time_rb

# Sorteio aleatório e operações na árvore
for _ in range(50000):
    random_num = random.randint(-9999, 9999)

    if random_num % 3 == 0:
        # Inserir na árvore
        avl_tree[random_num] = None
        rb_tree[random_num] = None
    elif random_num % 5 == 0:
        # Remover da árvore
        avl_tree.pop(random_num, None)
        rb_tree.pop(random_num, None)
    else:
        # Contar o número de ocorrências
        count_avl = avl_tree.get(random_num, 0)
        count_rb = rb_tree.get(random_num, 0)

# Medição do tempo e comparação
print(f"Tempo de inserção AVL: {insertion_time_avl} segundos")
print(f"Tempo de inserção Rubro-Negra: {insertion_time_rb} segundos")
