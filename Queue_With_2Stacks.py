# Problem : Implement a Queue using two stacks.
class Queue_with_Stack(object):

    def __init__(self):
        self.instack = []
        self.outstack = []

    def enqueu(self, item):
        self.instack.append(item)
        print('Stack1 =',self.instack)

    def dequeue(self):
        if not self.outstack:  # Means the outstack is empty
            while self.instack:  # Means loop through till instack has an element
                # Pop all the elements of instack and push into outstack ( Like if instack =[1,2,3] then outstack will have [3,2,1] )
                self.outstack.append(self.instack.pop())
            print('Stack2 =',self.outstack)

        # As per above comment it will product 1,2 and 3 on pop ( FIFO of Queue)
        return self.outstack.pop()


if __name__ == '__main__':
    q = Queue_with_Stack()
    q.enqueu(2)
    q.enqueu(3)
    q.enqueu(5)
    print('Removing one item from Queue (FIFO): ',q.dequeue())