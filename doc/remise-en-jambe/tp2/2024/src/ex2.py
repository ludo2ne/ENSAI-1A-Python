"""
Remise en jambe - TP Noté
12/09/2024
Élève 1 : ?
Élève 2 : ?
"""


def is_valid_password(pwd, bonus) -> bool:
    """Check if a password is valid
    bonus: boolean indicating whether the bonus is on or not"""

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

    if not bonus and max(digits.values()) >= 2:
        return True
    elif bonus and 2 in digits.values():
        return True
    else:
        return False


def count_valid_password(start, end, bonus) -> int:
    """Count the number of valid password between start and end
    bonus: boolean indicating whether the bonus is on or not"""

    if not isinstance(start, int) or not isinstance(end, int):
        raise TypeError("At least one of the 2 parameters is not an integer.")

    if len(str(start)) != 6 or len(str(end)) != 6:
        raise ValueError("Parameters must have exactly 6 digits.")

    nb_valid = 0  # intialize the counter

    for pwd in range(start, end + 1):
        if is_valid_password(pwd, bonus):
            nb_valid += 1

    return nb_valid


if __name__ == "__main__":

    resultat = count_valid_password(153517, 630395, bonus=False)
    print(resultat)  # obtained result : 1729

    bonus = count_valid_password(153517, 630395, bonus=True)
    print(bonus)  # Bonus : 1172
