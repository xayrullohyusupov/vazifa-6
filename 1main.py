class MyClass:
    def __init__(self, num):
        self.num = num
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < self.num:
            self.current += 1
            return self.current
        else:
            raise StopIteration


my_class = MyClass(5)

for i in my_class:
    print(i)
