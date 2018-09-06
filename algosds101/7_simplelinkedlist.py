

######          #######         #########
# 5    #        #  8            # -29
# next    --->  #  next ----->  # next ------> NONE
######          #######         #########



class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def __str__(self):
        return "Node({}, {})".format(self.data, self.next)

class LinkedList:
    def __init__(self, alist=None):
        self.head = None

        if alist:
            for el in alist:
                self.append(el)

    def prepend(self, data):
        node = Node(data)
        node.next = self.head
        self.head = node

    def append(self, data):
        node = Node(data)
        if self.head:
            n = self.head
            while n.next != None:
                n = n.next
            n.next = node
        else:
            self.head = node

    def length(self):
        n = self.head
        res = 0
        while n:
            res += 1
            n = n.next
        return res

    __len__ = length

    def find(self, data):
        n = self.head
        while n:
            if n.data == data:
                return True
            n = n.next
        return False

    __contains__ = find


    def __str__(self):
        return str(self.head)


def main():
    ll = LinkedList([1,2,3,4,5])
    print(ll)

    print(len(ll))
    print(5 in ll)
    print(7 in ll)
    


if __name__ == '__main__':
    main()