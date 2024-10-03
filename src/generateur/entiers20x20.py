import random

# Générer 20 lignes de 20 nombres entre 1 et 5000
for _ in range(20):
    line = [str(random.randint(1, 5000)) for _ in range(20)]
    print(" ".join(line))
