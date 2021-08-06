digit = input()

try:
    int(digit)
    for i in range(len(digit)):
        if (len(digit) - i > 1 and digit[i] == digit[i + 1]):
            print('da')
            exit()

    print('net')
except ValueError:
    print('net vvoda')