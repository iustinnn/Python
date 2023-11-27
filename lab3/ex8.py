def loop(mapping):
    result = []
    visited = set()

    current_key="start"
    while current_key not in visited:
        visited.add(current_key)
        if current_key != mapping[current_key]:
            result.append(mapping[current_key])
        current_key = mapping[current_key]
    return result

def main():
    sequence = loop({'start': 'a', 'b': 'a', 'a': '6', '6': 'z', 'x': '2', 'z': '2', '2': '2', 'y': 'start'})
    print(sequence)

if __name__ == '__main__':
    main()

