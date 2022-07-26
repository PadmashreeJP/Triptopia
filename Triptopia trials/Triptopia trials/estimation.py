class estimation():
    def __init__(self):
        self.estimation=[]
    def push(self,a):
        self.estimation.append(a)
    def pop(self):
        return self.estimation.pop()
    def peek(self):
        return self.estimation[len(self.estimation)-1]
    def size(self):
        return len(self.estimation)
    def display(self,a):
        return (self.estimation[a])
            

#e=estimation()
#e.push(100)
#e.display(0)
