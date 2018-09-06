class Stack:
    def __init__(self):
        self.backend = []

    def top(self):
        return self.backend[-1]

    def push(self, el):
        self.backend.append(el)

    def pop(self):
        if self.backend:
            return self.backend.pop()

    def __len__(self):
        return len(self.backend)

    def __str__(self):
        s = ""
        if self.backend:
            for el in self.backend[::-1]:
                s += "-----\n{el}\n"
        else:
            return "----\nEMPTY----\n"

        return s


# EASY
def reverse_str(astring):
    stk = Stack()
    for c in astring:
        stk.push(c)
    
    rev_str = ""
    while len(stk):
        rev_str += stk.pop()

    return rev_str
    

# MID
def reverse_int(n):
    stk = Stack()

    # 482 % 10 => 2, 482//10 -> 48

    while n>10:
        stk.push(n%10)
        n //= 10
    stk.push(n)
    
    revnum = 0

    tenth = 1
    while len(stk):
        n = stk.pop()
        revnum += tenth*n
        tenth *= 10 
    return revnum


def main():
    print(reverse_int(419))
    print(reverse_str("Hello, World"))

if __name__ == '__main__':
    main()