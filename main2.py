def print_factors():
    x = int(input("Enter a number: "))
    factors = []
    for i in range(1, x + 1):
        if x % i == 0:
            factors.append(i)
    print("The factors of", x, "are:", factors)

print_factors()