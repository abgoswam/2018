class MyClass(object):
    class_var = 1

    def __init__(self, i_var):
        self.i_var = i_var


foo = MyClass(2)
bar = MyClass(3)

print(foo.class_var)
print(bar.class_var)

print(foo.i_var)
print(bar.i_var)

print(MyClass.__dict__)
print(foo.__dict__)
