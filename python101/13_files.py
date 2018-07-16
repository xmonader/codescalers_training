# READ/WRITE TO A FILE..


# open, r, a, w

# file write, read, lines, looping on file


filename = "/home/ahmed/testfile1.txt"
f = open(filename, "w")
f.write("google.com")
f.write("yahoo.com")

f.close()

with open(filename, "w") as f:
    f.write("google.com\n")
    f.write("yahoo.com\n")


filename = "/home/ahmed/testfile1.txt"
f = open(filename, "r")
# f.write("google.com\n")
# f.write("yahoo.com\n")
for line in f:
    print(line)


