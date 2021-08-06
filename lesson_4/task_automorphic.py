number = int(input())  # int(input())


def get_numbers_count(number):
    count = 0
    while number:
        count += 1
        number = number // 10
    return count


def get_automorphic_numbers(max_number):
    for x in range(1, max_number + 1):
        square = x * x
        length_of_x = get_numbers_count(x)

        num_div = 10 ** length_of_x
        num = square % num_div

        if num == x:
            yield num


for x in get_automorphic_numbers(number):
    print(x, "*", x, "=", x * x)