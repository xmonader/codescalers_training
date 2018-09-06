def find_first_repeated(arr):
    found = {}

    for el in arr:
        if el in found:
            return el
        else:
            found[el] = True


def main():
    l = [1, 2, 3, 3, 4, 5]
    print(find_first_repeated(l))

if __name__ == '__main__':
    main()