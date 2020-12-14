
module_masses = "module_mass.txt"
# module_masses = "module_mass_test.txt"


def get_file_data(filename: str) -> list:
    with open(filename, "r") as file:
        return [int(line.strip()) for line in file]


def get_req_fuel(module: int) -> int:
    return int(module / 3) - 2


def main():
    module_mass_list = get_file_data(module_masses)
    fuel_list = map(get_req_fuel, module_mass_list)
    print(sum(fuel_list))


if __name__ == '__main__':
    main()
