import random
import statistics


def compute_mean_and_std(n):
    """
    Génération aléatoire de n nombres réels de [0;1)

    Parameters
    ----------
    n : int
        nombre d'éléments de nombres aléatoires

    Return
    ------
    Chaine contenant la moyenne et l'écart-type

    """
    L = [random.random() for _ in range(n)]
    return f"Moyenne    : {statistics.mean(L)} \nEcart type : {statistics.pstdev(L)}"


def test_fonction_randint(a, b, n):
    """Vérification de la qualité de la méthode randint

    Parameters
    ----------
    a : int
        borne inférieure
    b : int
        borne supérieure
    n : int
        nombre de tirages

    Returns
    -------
    dict : dictionnaire contenant les valeurs tirées et leurs fréquences

    Examples
    --------
    >>> a = 1
    >>> b = 5
    >>> n = 100000
    >>> nb = b - a + 1
    >>> marge_erreur = 0.05
    >>> freq_theorique = n / nb
    >>> dico = test_fonction_randint(a, b, n)
    >>> all([(((freq_empirique - freq_theorique) / freq_theorique) < marge_erreur) for freq_empirique in dico.values()])
    True


    """
    L = [random.randint(a, b) for _ in range(n)]
    dico = {}
    for v in set(L):
        dico[v] = L.count(v)
    return dico


def genadn(n):
    """
    Générer une chaine ADN composée des éléments : A, C, G, T

    Parameters
    ----------
    n : int
        Longueur de la chaine

    Returns
    -------
    str : la chaine ADN

    """
    adn = ""
    for _ in range(n):
        i = random.randint(1, 4)
        match i:
            case 1:
                adn += "G"
            case 2:
                adn += "T"
            case 3:
                adn += "A"
            case 4:
                adn += "C"
    return adn


def permut(liste):
    """Retourner une liste permutant aléatoirement les éléments
    de la liste donnée en entrée

    Parameters
    ----------
    liste : list
       liste quelconque

    Returns
    -------
    list
        une permutation de la liste d'entrée
    """
    res = []
    copie = liste[:]

    for i in range(len(liste)):
        random_element = copie.pop(random.randint(0, len(copie) - 1))
        res.append(random_element)

    return res


if __name__ == "__main__":
    print(compute_mean_and_std(100_000))

    print(test_fonction_randint(1, 5, 100_000))

    import doctest

    doctest.testmod(verbose=False)

    a = genadn(100)
    print(a)
    print("".join(permut(list(a))))
    print("".join(permut(list(a))))
    print("".join(permut(list(a))))
    print("".join(permut(list(a))))
    print("".join(permut(list(a))))
    print()
    print("".join(random.sample(list(a), len(a))))
