
def system_2_and_8(number, system):
    if system == 2:
        number_2 = []
        while number != 0:
            number_2.insert(0, number % 2)
            number //= 2
        return number_2
    elif system == 8:
        number_8 = []
        while number != 0:
            number_8.insert(0, number % 8)
            number //= 8
        return number_8

number = int(input("Enter number: "))
system = int(input("Enter system: "))
print(system_2_and_8(number, system))