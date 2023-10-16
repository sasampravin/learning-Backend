class stack():
    def __init__(self):
        self.stack=[]
        self.nit=0
    def isEmpty(self):
        return self.stack==[]
    def push(self,data):
        self.stack.insert(self.nit,data)
        self.nit+=1
        return '{} pushed to stack'.format(data)
    def pop(self):
        self.nit-=1
        data=self.stack.pop(self.nit)
        return '{} pop from stack'.format(data)
    def stacksize(self):
        return len(self.stack)

#testing
if __name__=='__main__':
    s=stack()
    print(s.push(2))
    print(s.push(8))
    print(s.push(3))
    print(s.push(9))
    print(s.pop())
    print(s.pop())
    print('size of the atack:',s.stacksize())
    
