
start = 124075
end = 580769


def check_adjacent(number: int) -> bool:
    num_list = list(str(number))
    for i in range(0, len(num_list)):
        # check adjacent digits are the same
        if i+1 < len(num_list):
            if num_list[i] == num_list[i+1]:
                return True
    return False


def check_no_decrease(number: int) -> bool:
    num_list = list(str(number))
    for i in range(0, len(num_list)):
        if i+1 < len(num_list):
            if num_list[i+1] < num_list[i]:
                return False
    return True


def main():
    password_list = []
    for number in range(start, end+1):
        adjacent = check_adjacent(number)
        no_decrease = check_no_decrease(number)
        if (adjacent is True) and (no_decrease is True):
            password_list.append(number)
    print(password_list)
    print(len(password_list))


if __name__ == '__main__':
    main()
