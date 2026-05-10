class Stack:
    def __init__(self,size):
        self.stack=[0]*size
        self.size=size
        self.top=-1
    def push(self,value):
        if self.top==self.size-1:
            print("stack overflow")
        else:
            self.top=self.top+1
            self.stack[self.top]=value
        print(value,"pushed to stack")
    def pop(self):
        if self.top==-1:
            print("stack underflow")
        else:
            value=self.stack[self.top]
            self.top=self.top-1
            print(value,"popped from stack")
    def peek(self):
        if self.top==-1:
            print("stack is empty")
        else:
            value=self.stack[self.top]
            print(value,"is the top element of stack")
    def isEmpty(self):
        if self.top==-1:
            print("stack is empty")
        else:
            print("stack is not empty")
    def isFull(self):
        if self.top==self.size-1:
            print("stack is full")
        else:
            print("stack is not full")
    def display(self):
        if self.top==-1:
            print("stack is empty")
        else:
            print("stack elements are:")
            for i in range(self.top,-1,-1):
                print(self.stack[i])
# Example usage:
if __name__=="__main__":
    stack=Stack(5)
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)
    stack.push(5)
    stack.push(6)  # This will cause stack overflow
    stack.display()
    stack.peek()
    stack.pop()
    stack.pop()
    stack.display()
    stack.isEmpty()
    stack.isFull()

    #time complexity: O(1) for push, pop, peek, isEmpty, isFull
    #space complexity: O(n) where n is the size of the stack

    


