
module_masses = "module_mass.txt"
# module_masses = "module_mass_test.txt"


def get_file_data(filename: str) -> list:
    with open(filename, "r") as file:
        return [int(line.strip()) for line in file]


def get_req_fuel(module: int) -> int:
    return int(module / 3) - 2


def get_req_fuel_recur(mass: int, fuel_sum=0) -> int:
    fuel = int(mass / 3) - 2
    print(fuel)
    if fuel <= 0:
        return fuel_sum
    else:
        fuel_sum += fuel
        return get_req_fuel_recur(fuel, fuel_sum)


def main():
    module_mass_list = get_file_data(module_masses)
    fuel_list = map(get_req_fuel, module_mass_list)
    print(sum(fuel_list))
    re_fuel_list = map(get_req_fuel_recur, module_mass_list)
    print(sum(re_fuel_list))


if __name__ == '__main__':
    main()
