def count_characters(text):
    char_count = {}

    for char in text:
        char_count[char] = char_count.get(char, 0) + 1
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    return char_count

def main():

    input_text = "Ana has apples."
    character_counts = count_characters(input_text)
    print(character_counts)
if __name__ == '__main__':
    main()
