def print_numbers():
    file = open("numbers.txt", "r")
    content = file.read()
    file.close()

    numbers = content.split(",")

    for number in numbers:
        print(number)


if __name__ == '__main__':
    print_numbers()
