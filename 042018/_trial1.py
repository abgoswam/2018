class Person:
    age = 23
    name = 'Adam'

    def get_name(self):
        return self.name


person = Person()

print('Person has age?:', hasattr(person, 'age'))
print('Person has salary?:', hasattr(person, 'salary'))
print('Person has get_name?:', hasattr(person, 'get_name'))
print('Person has set_name?:', hasattr(person, 'set_name'))
