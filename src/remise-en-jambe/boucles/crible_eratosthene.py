def crible_eratosthene(n) -> list[int]:

    # Initialisation de la liste des booléen de 0 à n-1
    liste_nombres = [True] * (n + 1)
    liste_nombres[0] = liste_nombres[1] = False

    for i in range(2, int(n**0.5) + 1):  # On parcourt la liste jusqu'au milieu
        if liste_nombres[i]:  # Si le ième nombre est premier,
            for j in range(i * i, n + 1, i):  # On élimine tous ses multiples
                liste_nombres[j] = False

    liste_nombres_premiers = []
    for i, v in enumerate(liste_nombres):
        if v:
            liste_nombres_premiers.append(i)

    # Écriture condensée
    # liste_nombres_premiers = [i for i, is_prime in enumerate(liste_nombres) if is_prime]

    return liste_nombres_premiers


def afficher_liste(liste) -> None:
    for i in liste:
        print(i, end=" ")


if __name__ == "__main__":
    a = crible_eratosthene(100)
    afficher_liste(a)
