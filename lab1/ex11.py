def count_words_in_text(text):
    words = text.split()
    return len(words)

def main():
    text = "Am un examen la python"
    word_count = count_words_in_text(text)
    print(f"Number of words in the text: {word_count}")

if __name__ == '__main__':
    main()
