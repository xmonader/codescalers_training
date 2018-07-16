# DIV BY 0


# PASSING WRONG VALUE TO A FUNCTION

# def add1(num):
#     if type(num) == int:
#         return num + 1
#     else:
#         raise ValueError("num should be int")

def trydiv():
    num1 = input("Enter first num: ")
    num2 = input("Enter second num: ")

    if num1.isdigit() and num2.isdigit():
        i1 = int(num1)
        i2 = int(num2)
        if i2 == 0:
            raise ValueError("i2 is zero..")
        return i1/i2
    else:
        raise ValueError("i1, i2 aren't numbers..")

def trymul():
    num1 = input("Enter first num: ")
    num2 = input("Enter second num: ")

    if num1.isdigit() and num2.isdigit():
        i1 = int(num1)
        i2 = int(num2)
        return i1* i2
    else:
        raise ValueError("i1, i2 aren't numbers..")


def program():
    while True:
        operation = input("Enter operation")
        try:
            if operation == "/":
                trydiv()
            elif operation == "*":
                trymul()
        except Exception as e:
            print("Exception happened", e)


# OPEN FILE DOESNT EXIST


