def pyramide(n):
    for k in range(n):
        print((k * " " + (2 * (n - k) - 1) * "*"))


if __name__ == "__main__":
    pyramide(10)
