
from timey import timed 

# f(n)	Name
# 1	Constant
# n	Linear





## const
@timed
def my_add(x,y):
    return x+y



## const
@timed
def my_calc_(x,y, op='+'):
    if op == '+':
        return x+y
    elif op == '-':
        return x-y
    else:
        raise NotImplementedError()


# N
@timed
def find_element(el, seq):
    for i, current_el in enumerate(seq):
        if current_el == el:
            return i
    return -1


# N
## sum elements.
@timed
def my_linear(until):
    totalsum = 0
    for el in range(until):
        totalsum += el
    
    return totalsum




def main():
    my_add(3, 5)
    my_add(5, 15)


    # best case
    find_element(1, range(10000000))
    find_element(50, range(10000000))
    find_element(500, range(10000000))
    # worst case 
    find_element(10000000, range(10000000))



    my_linear(10)
    my_linear(100)
    my_linear(1000)
    my_linear(100000)
    my_linear(1000000)
    my_linear(10000000)


if __name__ == '__main__':
    main()