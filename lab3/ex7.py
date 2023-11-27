def set_operations(*sets):
    result = {}
    for i in range(len(sets)):
        for j in range(i+1, len(sets)):
            set1 = sets[i]
            set2 = sets[j]

            union = set1 | set2
            intersection = set1 & set2
            diff1 = set1 - set2
            diff2 = set2 - set1

            key1 = f"{set1} | {set2}"
            key2 = f"{set1} & {set2}"
            key3 = f"{set1} - {set2}"
            key4 = f"{set2} - {set1}"

            result[key1] = union
            result[key2] = intersection
            result[key3] = diff1
            result[key4] = diff2

    return result

def main():
    set1 = {1, 2}
    set2 = {2, 3}
    result = set_operations(set1, set2)
    print(result)

if __name__ == '__main__':
    main()
