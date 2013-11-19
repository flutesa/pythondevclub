class Person:
    def __init__(self, name="", age=0):
        self.name = name
        self.age = age

    def birthday(self):
        self.age += 1

    def howold(self):
        return str(self.age)

    def whatisyourname(self):
        return self.name

    def __str__(self):
        return self.howold() + ' ' + self.whatisyourname()


a = person(age=10, name="John")
for i in range(10):
    a.birthday()
print(a.age)
