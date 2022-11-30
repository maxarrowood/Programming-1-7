def main():
    eggs = int(input("Eggs purchased: "))
    dozens = eggs // 12
    remain = eggs % 12
    price = 0.0
    cost = 0.0

    if dozens > 0 and dozens < 4:
        price = 0.50
    elif dozens >= 4 and dozens < 6:
        price = 0.45
    elif dozens >= 6 and dozens < 11:
        price = 0.40
    elif dozens >= 11:
        price = 0.30

    expr = price * 0.083
    re = remain * expr
    cost = price * dozens + re
    print("Total cost is $" + str(round(cost, 2)))


if __name__ == "__main__":
    main()
