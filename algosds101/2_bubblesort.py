from timey import timed
import random


@timed
def bubble(arr):
    for pas in range(len(arr)):
        for i in range(1, len(arr)):
            if arr[i-1] > arr[i]:
                arr[i], arr[i-1] = arr[i-1], arr[i]
        # print(f"After pass {pas}: arr {arr}")


def main():
    for inp in [100, 1000, 10000, 100000, ]:
        bubble([random.randint(0,inp) for x in range(inp)])

if __name__ == '__main__':
    main()
