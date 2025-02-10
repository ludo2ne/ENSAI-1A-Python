def list_new_mat(nl, nc):
    """Crée et retourne une matrice de dimensions nl x nc remplie de 0."""
    return [[0] * nc for _ in range(nl)]


def list_set_mat(m, i, j, x):
    """Affecte la valeur x à la case (i, j) de la matrice m."""
    if 0 <= i < len(m) and 0 <= j < len(m[0]):
        m[i][j] = x


def list_get_mat(m, i, j):
    """Retourne la valeur à la case (i, j) de la matrice m."""
    if 0 <= i < len(m) and 0 <= j < len(m[0]):
        return m[i][j]
    return None


def print_mat(m):
    """Affiche une matrice m"""
    max_width = max(len(str(cell)) for row in m for cell in row)

    for row in m:
        print(" ".join(f"{cell:>{max_width}}" for cell in row))
