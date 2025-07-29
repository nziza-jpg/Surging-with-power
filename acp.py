def powerof8(number):
    count = 0
    if (number & (number - 1)) != 0 or number == 0:
        return False
    while (number > 1):
        number >>= 1
        count += 1
    if (count % 3 == 0):
        return True
    else:
        return False

# Input and output
number = int(input("Enter your number: "))
if powerof8(number):
    print(number, "is a power of 8")
else:
    print(number, "is not a power of 8")