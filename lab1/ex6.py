def spiral_matrix_to_string(matrix):
    result = []
    while matrix:
        result += matrix[0]
        matrix = list(zip(*matrix[1:]))[::-1]  #exclude prima col rotate 90, reverse transposed - last
    return ''.join(result)

def main():
    matrix = [
        ['f', 'i', 'r', 's'],
        ['n', '_', 'l', 't'],
        ['o', 'b', 'a', '_'],
        ['h', 't', 'y', 'p']
    ]

    output_string = spiral_matrix_to_string(matrix)
    print("Spiral order string:", output_string)
if __name__ == '__main__':
    main()
