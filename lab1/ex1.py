import math


def find_gcd():
    numbers = input("Numerele cu spatiu: ").split()
    numbers = [int(num) for num in numbers]
    gcd = math.gcd(*numbers) #separate args
    print("GCD:", gcd)

def main():
    find_gcd()

if __name__ == '__main__':
    main()
