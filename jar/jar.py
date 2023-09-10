class Jar:
    def __init__(self, capacity=12):
        self.n = 0
        if(capacity>=0):
            self.cap = capacity;
        else:
            raise ValueError
        ...

    def __str__(self):
        return "🍪"*self.n
    
        ...

    def deposit(self, n):
        if(self.n +n > self.cap):
            raise ValueError
        else:
            self.n += n
        ...

    def withdraw(self, n):
        if(n > self.n):
            raise ValueError
        else:
            self.n -= n 
        ...

    @property
    def capacity(self):
        return self.cap
        ...

    @property
    def size(self):
        return  self.n
        ...
        
        
def main():
    jar = Jar()
    print(jar)
    jar.deposit(1)
    print(jar)
    jar.deposit(11)
    print(jar)
    jar.withdraw(2)
    print(jar)
    jar.withdraw(11)
    print(jar)
    jar.deposit(12)
    print(jar)
    jar.deposit(1)
    print(jar)
    jar.withdraw(12)
    
if __name__ == "__main__":
    main()