import re
from collections import Counter

def most_common_letter(text):
    text = re.sub(r'[^A-Za-z]', '', text)  # el caractere non alfabetice
    letter_counts = Counter(text.lower())
    most_common = letter_counts.most_common(1)[0] #singuru
    return most_common[0], most_common[1]#most common, freq in list

def main():
    text = "marul nu e fruct"
    letter, count = most_common_letter(text)
    print(f"The most common letter is '{letter}' with {count} occurrences.")

if __name__ == '__main__':
    main()
