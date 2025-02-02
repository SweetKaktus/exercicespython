def double_values(number_list_to_double: list[int] = range(20)):
    return [element * 2 for element in number_list_to_double]


if __name__ == "__main__":
    print(double_values([13, 52, 3, 9, 46]))
    pass