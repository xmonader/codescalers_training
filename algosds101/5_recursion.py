def mylen(arr):
    arrlen = 0
    for el in arr:
        arrlen += 1

    return arrlen


def mylen_rec(arr):
    if arr == []:
        return 0
    else:
        return 1 + mylen_rec(arr[1:])
    
def mysum(arr):
    total = 0
    for el in arr:
        total += el

    return total 

def mysum_rec(arr):
    if arr == []:
        return 0
    else:
        return arr[0] + mysum_rec(arr[1:])
    

def main():
    print(mylen([124,2,2,189,2]))    
    print(mylen_rec([124,2,2,189,2]))    
    

    print(mysum([124,2,2,189,2]))    
    print(mysum_rec([124,2,2,189,2]))    


if __name__ == '__main__':
    main()