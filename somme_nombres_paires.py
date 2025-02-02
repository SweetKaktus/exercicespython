from pprint import pprint


def sum_pair_numbers(cap_number: int = 20):
    list_numbers = range(cap_number)
    list_pair_numbers = [element for element in list_numbers if element % 2 == 0]
    sum_pairs = 0
    for element in list_pair_numbers:
        sum_pairs += element
    return sum_pairs

if __name__ == "__main__":
    pprint(sum_pair_numbers(12))