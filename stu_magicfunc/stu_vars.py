class A(object):
    def __init__(self):
        self.b = 900


a = A()
d = {"__classname__": type(a).__name__}
d.update(vars(a))

print(vars(a))  # {'b': 900}
print(d)  # {'__classname__': 'A', 'b': 900}
