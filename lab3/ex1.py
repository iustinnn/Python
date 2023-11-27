def set_operations(a, b):
    intersection = set(a) & set(b)
    union = set(a) | set(b)
    a_minus_b = set(a) - set(b)
    b_minus_a = set(b) - set(a)

    return [intersection, union, a_minus_b, b_minus_a]

def main():
    list_a = [1, 2, 3, 4, 5]
    list_b = [3, 4, 5, 6, 7]

    result = set_operations(list_a, list_b)

    print(result)

if __name__ == '__main__':
    main()
