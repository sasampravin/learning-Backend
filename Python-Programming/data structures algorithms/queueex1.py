class Queue():
    def __init__(self):
        self.queue=[]
    def isEmpty(self):
        return self.queue==[]
    def enqueue(self,data):
        self.queue.insert(0,data)
        return '{} is added to queue'.format(data)
    def dequeue(self):
        return self.queue.pop()
    def sizeofqueue(self):
        return '{} size of queue'.format(len(self.queue))

if __name__=='__main__':
    q=Queue()
    print(q.enqueue(1))
    print(q.enqueue(6))
    print(q.enqueue(2))
    print(q.dequeue())
    print(q.dequeue())
    print(q.sizeofqueue())
    print(q.isEmpty())
