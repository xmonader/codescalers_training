# COUNTING TO 0 - 10 and down AND a python as calculator
# ON LISTS AND ON DICTS


# while True:
#     print("dmdm")


# print_count = 0

# while print_count < 10:
#     print("dmdm")


print_count = 0

while print_count < 10:
    print("dmdm")
    print_count = print_count + 1 
    # print_count += 1

# for i in range(10):
#     print("dmdm")



# # range(10)
# # range(2,10)
# range(3, 15, 2)



# total = 0
# for num in range(10):
#     total = total + num # old total + new number

#     print("num: ", num, "total: ", total)



mynums = [5, 214, 2, 120, 9, 12, 3, 0]
min_num = mynums[0] ### -> 5

for num in mynums:
    if num < min_num:
        min_num = num
    print("num: ", num, "MIN NUM: ", min_num)
