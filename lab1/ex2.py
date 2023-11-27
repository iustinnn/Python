def count_vowels(string):
    vowels = "AEIOUaeiou"
    count = 0
    for char in string:
        if char in vowels:
            count += 1
    return count

def main():
    input_string = input("string:")
    vowel_count = count_vowels(input_string)
    print("nr vocale:", vowel_count)

if __name__ == '__main__':
    main()
