from timey import timed


@timed
def bsearch(arr, el):
    low = 0
    high = len(arr)-1

    while low < high and arr[high] > el:
        mid = low + (high-low)//2
        midel = arr[mid]
        if midel == el:
            return mid
        elif el > midel:
            low = mid
        else:
            high = mid
        
    return -1


print(bsearch([3,4,5,7,8, 9, 10], 8))
            


def main():
    l = list(range(50))
    print(l)
    print(bsearch(l, 25))
    print(bsearch(l, 0))
    print(bsearch(l, 100))
    

if __name__ == '__main__':
    main()