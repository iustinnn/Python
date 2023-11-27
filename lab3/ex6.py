def count_unique_and_duplicates(input_list):
    unique_set = set()
    duplicates_set = set()

    for item in input_list:
        if item in unique_set:
            duplicates_set.add(item)
            unique_set.remove(item)
        else:
            unique_set.add(item)

    return len(unique_set), len(duplicates_set)

def main():

    my_list = [1, 2, 3, 4, 2, 2, 4, 5]
    result = count_unique_and_duplicates(my_list)
    print(result)

if __name__ == '__main__':
    main()
