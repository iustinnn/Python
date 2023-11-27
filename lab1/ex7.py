def is_palindrome(number):
    str_num = str(number)
    return str_num == str_num[::-1]

def main():

    num = int(input("Enter a number: "))
    if is_palindrome(num):
        print("The number is a palindrome.")
    else:
       print("The number is not a palindrome.")

if __name__ == '__main__':
    main()
