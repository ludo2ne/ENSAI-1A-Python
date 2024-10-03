def fibonacci(n):
    return n if n < 2 else fibonacci(n - 1) + fibonacci(n - 2)


def afficher_suite_fibonacci(n) -> None:
    """Affiche les n premiers termes de la suite de Fibonacci"""
    if not isinstance(n, int) or n <= 0:
        raise TypeError("Erreur : n doit être strictement positif")
    a, b = 0, 1
    for _ in range(n):
        print(a, end=" ")
        b, a = a + b, b


if __name__ == "__main__":
    afficher_suite_fibonacci(15)
