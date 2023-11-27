import re

def extract_number_from_text(text):
    match = re.search(r'\d+', text)  #digits, raw string
    if match:
        return int(match.group())
    else:
        return None

def main():
    text = "An apple is 123 USD"
    number = extract_number_from_text(text)
    if number is not None:
       print("Extracted number:", number)
    else:
       print("No number found in the text.")

if __name__ == '__main__':
    main()
