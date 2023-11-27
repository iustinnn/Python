def count_set_bits(number):
    binary_representation = bin(number)
    count = binary_representation.count('1')
    return count

def main():
    num = 24
    bit_count = count_set_bits(num)
    print(f"Number of set bits in {num}: {bit_count}")

if __name__ == '__main__':
    main()
