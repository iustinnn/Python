def count_occurrences(first_str, second_str):
    count = second_str.count(first_str)
    return count

def main():

    first_string = input("Enter the first string: ")
    second_string = input("Enter the second string: ")
    occurrences = count_occurrences(first_string, second_string)
    print("Number of occurrences:", occurrences)

if __name__ == '__main__':
    main()
