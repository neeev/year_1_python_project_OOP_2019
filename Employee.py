class IterEmployee(type):
    def __iter__(cls):
        return iter(cls._employees)


class Employee(metaclass=IterEmployee):
    _employees = []

    def __init__(self, no, n, a, p, s, y):
        self._employees.append(self)

        self.enum = no
        self.name = n
        self.age = a
        self.position = p
        self.salary = s
        self.years = y

    def deleterecord(self, i):
        del self._employees[i]

    @property
    def enum(self):
        return self.__enum

    @enum.setter
    def enum(self, no):
        self.__enum = no

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, n):
        self.__name = n

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, a):
        self.__age = a

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, p):
        self.__position = p

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, s):
        self.__salary = s

    @property
    def years(self):
        return self.__years

    @years.setter
    def years(self, y):
        self.__years = y
