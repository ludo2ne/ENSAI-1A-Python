def convertir_base(entier_base_10, nouvelle_base) -> str:
    if not (2 <= nouvelle_base <= 16):
        raise ValueError("La base doit être comprise entre 2 et 16.")

    if entier_base_10 < 0:
        raise ValueError("L'entier doit être positif.")

    # Gestion du cas où l'entier est zéro
    if entier_base_10 == 0:
        return "0"

    chiffres = "0123456789ABCDEF"
    resultat = ""

    while entier_base_10 > 0:
        resultat = chiffres[entier_base_10 % nouvelle_base] + resultat
        entier_base_10 //= nouvelle_base

    return resultat


if __name__ == "__main__":
    print(convertir_base(2, 2))
    print(convertir_base(255, 16))
