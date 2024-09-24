"""
Remise en jambe - TP Noté
12/09/2024
Élève 1 : ?
Élève 2 : ?
"""


def is_valid_password(pwd) -> bool:
    """Check if a password is valid"""

    pwd_str = str(pwd)

    # Check that the numbers are in ascending order
    if list(pwd_str) != sorted(pwd_str):
        return False

    # Create a dictionary to count the number of digit occurrences
    digits = {}
    for d in pwd_str:
        if d in digits.keys():
            digits[d] += 1  # if the key exists, we increment the value
        else:
            digits[d] = 1  # if the key does not exist, initialize its value to 1

    # Check if at least one digit appears at least 2 times
    if max(digits.values()) >= 2:
        return True

    # Bonus : exactly a pair of a digit
    # replace the 2 lines above with :
    #
    # if 2 in digits.values():
    #     return True

    return False


def count_valid_password(start, end) -> int:
    """Count the number of valid password between start and end"""

    if not isinstance(start, int) or not isinstance(end, int):
        raise TypeError("At least one of the 2 parameters is not an integer.")

    if len(str(start)) != 6 or len(str(end)) != 6:
        raise ValueError("Parameters must have exactly 6 digits.")

    nb_valid = 0  # intialize the counter

    for pwd in range(start, end + 1):
        if is_valid_password(pwd):
            nb_valid += 1

    return nb_valid


if __name__ == "__main__":

    resultat = count_valid_password(153517, 630395)
    print(resultat)
    # résultat obtenu : 1729
    # Bonus : 1172
