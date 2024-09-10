def convertir_base(entier_base_10, nouvelle_base):

    if not (2 <= nouvelle_base <= 16):
        raise ValueError("La base doit être comprise entre 2 et 16")

    if entier_base_10 == 0:
        return "0"

    digits = "0123456789ABCDEF"
    res = ""

    while entier_base_10 > 0:
        reste = entier_base_10 % nouvelle_base
        res = digits[reste] + res
        entier_base_10 //= nouvelle_base  # partie entière du quotient

    return res


if __name__ == "__main__":

    print(convertir_base(255, 16))
    print(convertir_base(127, 2))
