from timey import timed
import random



def selection(arr):
    for i in range(len(arr)):
        _minidx = i
        for j in range(i, len(arr)):
            # print(arr, " I: ", i, " J: ", j, " MIN: ", _minidx)
            if arr[j] < arr[_minidx]:
                _minidx = j
        arr[i], arr[_minidx] = arr[_minidx], arr[i]
        # print("Found min: ", arr[_minidx], ", at idx: ", _minidx)
    
    return arr


def main():
    for inp in [10, 100, 1000, 10000]:
        selection([random.randint(0,inp) for x in range(inp)])

if __name__ == '__main__':
    main()