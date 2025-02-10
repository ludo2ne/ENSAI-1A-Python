def dict_new_mat(nl, nc):
    """Crée et retourne une matrice vide représentée par un dictionnaire."""
    return {}


def dict_set_mat(m, i, j, x):
    """Affecte la valeur x à la case (i, j) de la matrice m.
    Si x est 0, supprime l'élément de la matrice."""
    if x == 0:
        if (i, j) in m:
            del m[(i, j)]
    else:
        m[(i, j)] = x


def dict_get_mat(m, i, j):
    """Retourne la valeur à la case (i, j) de la matrice m.
    Retourne 0 si la case (i, j) n'existe pas."""
    return m.get((i, j), 0)


def print_dict_mat(m, nl, nc):
    """Affiche une matrice représentée par un dictionnaire."""
    max_width = max(len(str(val)) for val in m.values()) if m else 1

    for i in range(nl):
        row = []
        for j in range(nc):
            row.append(f"{m.get((i, j), 0):>{max_width}}")
        print(" ".join(row))
