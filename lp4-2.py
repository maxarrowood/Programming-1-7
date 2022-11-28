def main():
    kilos = int(input("Enter weight in Kilos: "))
    len = int(input("Enter length in cm: "))
    wid = int(input("Enter width in cm: "))
    high = int(input("Enter height in cm: "))
    cub = len * wid * high

    if cub >= 100000 and kilos >= 27:
        print("Too Large and Heavy")

    elif kilos >= 27:
        print("Too Heavy")

    elif cub >= 100000:
        print("Too Large")

    else:
        print("Will fit")
    pass


if __name__ == "__main__":
    main()
