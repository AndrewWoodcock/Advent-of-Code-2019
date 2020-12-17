
# intcode_data = "intcode_test.txt"
intcode_data = "intcode.txt"


def get_file_data(filename: str) -> list:
    with open(filename, "r") as file:
        return list(map(int, file.readline().split(",")))


def read_opcode(intcode: list) -> list:
    print(intcode)
    for i in range(0, len(intcode)):
        opcode = 0
        if i % 4 == 0:
            opcode = intcode[i]
            if opcode == 1:
                a = intcode[intcode[i+1]]
                b = intcode[intcode[i+2]]
                intcode[intcode[i+3]] = a + b
            if opcode == 2:
                a = intcode[intcode[i+1]]
                b = intcode[intcode[i+2]]
                intcode[intcode[i+3]] = a * b
            if opcode == 99:
                return intcode


def main():
    intcode_list = get_file_data(intcode_data)
    program_output = read_opcode(intcode_list)
    print("The value at position 0 after program halt is {0}".format(program_output[0]))


if __name__ == '__main__':
    main()
