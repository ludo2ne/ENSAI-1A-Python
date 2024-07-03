def est_pair(n) -> bool:
    if not isinstance(n, int):
        raise ValueError("Erreur : n doit être un entier")

    return n % 2 == 0


def est_pair_print(n) -> None:
    print(est_pair(n))


if __name__ == "__main__":
    est_pair_print(2)
    est_pair_print(-8)
    est_pair_print(5)
