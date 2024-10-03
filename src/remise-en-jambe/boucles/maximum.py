def maximum(*parametres):
    """Retourne le maximum d'une liste indéfinie de paramètres"""
    liste_parametres = []
    for param in parametres:
        liste_parametres.append(param)
    return max(liste_parametres)


if __name__ == "__main__":
    print(maximum(1, 12, 3, 50, 99, 53, 76))
    print(maximum("a", "C", "t"))
