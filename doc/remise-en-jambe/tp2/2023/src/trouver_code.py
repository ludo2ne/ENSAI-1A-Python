def trouver_code(texte, taille) -> int:
    """
    Fonction qui recherche la première occurence de n caractères consécutifs différents dans une chaine de caractères

    Paramétres :
      texte (str) : la chaine à tester
      taille (int) : le nombre de caractères consécutifs différents

    Sortie:
      int : position du dernier caractère de la première occurrence trouvée
    """

    # Liste pour stocker au fur et à mesure les caractères consécutifs que l'on va tester
    caracteres_consecutifs = []

    # Parcours de la chaine de caractères
    for i in range(len(texte)):
        caracteres_consecutifs.append(texte[i])  # On ajoute le caractère courant

        # Si trop de caractères, on supprime le plus "vieux"
        if len(caracteres_consecutifs) > taille:
            caracteres_consecutifs.pop(0)

        # Si tous les caractères sont différents et la taille est bonne, on affiche le résultat
        if len(set(caracteres_consecutifs)) == taille:
            return i + 1


def trouver_code_v2(texte, taille) -> int:
    """Même fonction en écriture condensée"""
    for i in range(taille, len(texte) + 1):
        if len(set(texte[i - taille : i])) == taille:
            return i


if __name__ == "__main__":
    # Import du fichier
    file_path = "annales/2023-2024/data/code.txt"
    with open(file_path, "r") as file:
        texte = file.read()

    print("Tests.....")
    print(trouver_code("jgngmnjdyigpmeawqksgcntozdpjiy", 4) == 7)
    print(trouver_code("vpqvdjfvapvbmlfjaxgdkqznphwt", 4) == 5)
    print(trouver_code("frfjfxjxflbxenxoervxbdnliftzuhjky", 4) == 10)
    print(trouver_code("ruxrxorrixjdbordjxfhivtzlekuynbo", 14) == 26)

    print("-" * 100)

    # Avec le fichier texte
    print(trouver_code(texte, 4))
    print(trouver_code(texte, 14))
