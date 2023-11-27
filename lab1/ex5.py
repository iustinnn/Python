import re
def convert_to_lowercase_with_underscores(input_string):
    result = re.sub(r'([a-z0-9])([A-Z])', r'\1_\2', input_string) #substitution
    return result.lower()

def main():
    input_string = input("Enter an UpperCamelCase string: ")
    formatted_string = convert_to_lowercase_with_underscores(input_string)
    print("Converted string:", formatted_string)

if __name__ == '__main__':
    main()
