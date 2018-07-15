
# Find the sum of all the multiples of 3 or 5 below 1000.

mynums = range(1000)

total = 0
for num in mynums:
    if num % 3 == 0 or num%5 == 0:
        print("Num :", num)
        total = total + num