def fizz_buzz(a) -> None:

    res = ""

    if a % 3 == 0:
        res += "FIZZ"
    if a % 5 == 0:
        res += " BUZZ"

    print(a, "\t : ", res.strip())


if __name__ == "__main__":
    fizz_buzz(4)
    fizz_buzz(9)
    fizz_buzz(10)
    fizz_buzz(15)
