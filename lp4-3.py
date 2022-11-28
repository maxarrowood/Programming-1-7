def main():
    eggs = int(input("Dozens of Eggs purchased: "))
    price = 0.0
    cost = 0.0

    if eggs > 0 and eggs < 4:
        price = 0.50
    elif eggs >= 4 and eggs < 6:
        price = 0.45
    elif eggs >= 6 and eggs < 11:
        price = 0.40
    elif eggs >= 11:
        price = 0.30

    cost = price * eggs
    print("Total cost is $" + str(round(cost, 2)))


if __name__ == "__main__":
    main()
