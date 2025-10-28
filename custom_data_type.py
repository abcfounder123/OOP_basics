"""
Custom data types

################################################

Kg
class   ->  Kg
data    ->  n
methods ->  add()

################################################

Step.1 (draw Kg Type)

class Kg:
    def __init__(self, n):
        self.n = n

    def add(self, other):
        pass

################################################

Step.2 (repr)
# 1Kg

class Kg:
    def __init__(self, n):
        self.n = n

    def add(self, other):
        pass

    def __repr__(self):
        return f"{self.n}Kg"


x = Kg(1)
y = Kg(2)
print(x, y)

################################################

Step.3 (add)
# 1Kg + 2Kg = 3Kg

class Kg:
    def __init__(self, n):
        self.n = n

    def add(self, other):
        return Kg(self.n + other.n)

    def __repr__(self):
        return f"{self.n}Kg"


x = Kg(1)
y = Kg(2)
z = x.add(y)
print(z)

################################################

Step.4 (+)
# x + y

class Kg:
    def __init__(self, n):
        self.n = n

    def __add__(self, other):
        return Kg(self.n + other.n)

    def __repr__(self):
        return f"{self.n}Kg"


x = Kg(1)
y = Kg(2)
z = x.__add__(y)
print(z)
print(x + y)

################################################

Create Lb

class Kg:
    def __init__(self, n):
        self.n = n

    def __add__(self, other):
        return Kg(self.n + other.n)

    def __repr__(self):
        return f"{self.n}kg"


class Lb:
    def __init__(self, n):
        self.n = n

    def __add__(self, other):
        return Lb(self.n + other.n)

    def __repr__(self):
        return f"{self.n}lb"


a = Lb(1)
b = Lb(2)
print(a + b)

################################################

Step.5 ( + -> Kg, Lb )
# Lb + Kg = Lb
# Kg + lb = Kg
# 1kg + 2.2lb = 2.0kg
# 2.2lb + 1kg = 4.4lb

class Kg:
    def __init__(self, n):
        self.n = n

    def __add__(self, other):
        if type(other) is Kg:
            return Kg(self.n + other.n)
        elif type(other) is Lb:
            return Kg(self.n + other.n / 2.2)

    def __repr__(self):
        return f"{self.n}kg"


class Lb:
    def __init__(self, n):
        self.n = n

    def __add__(self, other):
        if type(other) is Lb:
            return Lb(self.n + other.n)
        elif type(other) is Kg:
            return Lb(self.n + other.n * 2.2)

    def __repr__(self):
        return f"{self.n}lb"


a = Kg(1)
b = Lb(2.2)

print(a + b)
print(b + a)

################################################

Step.6 ( - )

class Kg:
    def __init__(self, n):
        self.n = n

    def __add__(self, other):
        if type(other) is Kg:
            return Kg(self.n + other.n)
        elif type(other) is Lb:
            return Kg(self.n + other.n / 2.2)

    def __sub__(self, other):
        if type(other) is Kg:
            return Kg(self.n - other.n)
        elif type(other) is Lb:
            return Kg(self.n - other.n / 2.2)

    def __repr__(self):
        return f"{self.n}kg"


class Lb:
    def __init__(self, n):
        self.n = n

    def __add__(self, other):
        if type(other) is Lb:
            return Lb(self.n + other.n)
        elif type(other) is Kg:
            return Lb(self.n + other.n * 2.2)

    def __sub__(self, other):
        if type(other) is Lb:
            return Lb(self.n - other.n)
        elif type(other) is Kg:
            return Lb(self.n - other.n * 2.2)

    def __repr__(self):
        return f"{self.n}lb"

################################################

Step.7 ( literal ) (2.2 .lb + 1 .kg)

from custom_literals import literal


class Kg:
    def __init__(self, n):
        self.n = n

    def __add__(self, other):
        if type(other) is Kg:
            return Kg(self.n + other.n)
        elif type(other) is Lb:
            return Kg(self.n + other.n / 2.2)

    def __sub__(self, other):
        if type(other) is Kg:
            return Kg(self.n - other.n)
        elif type(other) is Lb:
            return Kg(self.n - other.n / 2.2)

    def __repr__(self):
        return f"{self.n}kg"


class Lb:
    def __init__(self, n):
        self.n = n

    def __add__(self, other):
        if type(other) is Lb:
            return Lb(self.n + other.n)
        elif type(other) is Kg:
            return Lb(self.n + other.n * 2.2)

    def __sub__(self, other):
        if type(other) is Lb:
            return Lb(self.n - other.n)
        elif type(other) is Kg:
            return Lb(self.n - other.n * 2.2)

    def __repr__(self):
        return f"{self.n}lb"


@literal(int, float, name="kg")
def f1(n):
    return Kg(n)

@literal(int, float, name="lb")
def f2(n):
    return Lb(n)


# f1(2)  -> Kg(2)  -> 2kg
#  1 kg, 1.1 kg  -> f1


print(Kg(1) + Lb(2.2))
print(2.2 .lb + 1 .kg)

################################################

Step.8 ( ==, eq )

from custom_literals import literal


class Kg:
    def __init__(self, n):
        self.n = n

    def __add__(self, other):
        if type(other) is Kg:
            return Kg(self.n + other.n)
        elif type(other) is Lb:
            return Kg(self.n + other.n / 2.2)

    def __sub__(self, other):
        if type(other) is Kg:
            return Kg(self.n - other.n)
        elif type(other) is Lb:
            return Kg(self.n - other.n / 2.2)
        
    def __eq__(self, other):
        return self.n == self.n

    def __repr__(self):
        return f"{self.n}kg"


class Lb:
    def __init__(self, n):
        self.n = n

    def __add__(self, other):
        if type(other) is Lb:
            return Lb(self.n + other.n)
        elif type(other) is Kg:
            return Lb(self.n + other.n * 2.2)

    def __sub__(self, other):
        if type(other) is Lb:
            return Lb(self.n - other.n)
        elif type(other) is Kg:
            return Lb(self.n - other.n * 2.2)
        
    def __eq__(self, other):
        return self.n == self.n

    def __repr__(self):
        return f"{self.n}lb"


@literal(int, float, name="kg")
def f1(n):
    return Kg(n)

@literal(int, float, name="lb")
def f2(n):
    return Lb(n)


print(1 == 1)
print(1 .kg == 1 .kg)

################################################

Step.9 ( == of Kg and Lb )

from custom_literals import literal


class Kg:
    def __init__(self, n):
        self.n = n

    def __add__(self, other):
        if type(other) is Kg:
            return Kg(self.n + other.n)
        elif type(other) is Lb:
            return Kg(self.n + other.n / 2.2)

    def __sub__(self, other):
        if type(other) is Kg:
            return Kg(self.n - other.n)
        elif type(other) is Lb:
            return Kg(self.n - other.n / 2.2)

    def __eq__(self, other):
        if type(other) is Kg:
            return self.n == other.n
        elif type(other) is Lb:
            return self.n == other.n / 2.2

    def __repr__(self):
        return f"{self.n}kg"


class Lb:
    def __init__(self, n):
        self.n = n

    def __add__(self, other):
        if type(other) is Lb:
            return Lb(self.n + other.n)
        elif type(other) is Kg:
            return Lb(self.n + other.n * 2.2)

    def __sub__(self, other):
        if type(other) is Lb:
            return Lb(self.n - other.n)
        elif type(other) is Kg:
            return Lb(self.n - other.n * 2.2)

    def __eq__(self, other):
        if type(other) is Lb:
            return self.n == other.n
        elif type(other) is Kg:
            return self.n == other.n * 2.2

    def __repr__(self):
        return f"{self.n}lb"


@literal(int, float, name="kg")
def f1(n):
    return Kg(n)

@literal(int, float, name="lb")
def f2(n):
    return Lb(n)


print(1 == 1)
print(1 .kg == 1 .kg)
print(1 .lb == 1 .lb)
print(1 .kg == 2.2 .lb)
print(2.2 .lb == 1 .kg)

################################################

# 1 kg --> 10, 1000
# 1 -> 28 -> 280


x = 1 .lb   # Kg(1)    Mandalay
y = 1 .lb   # Kg(1)    Yangon
print(id(x))
print(id(y))
print(x is y)

################################################

Step.10 ( to reduce memory )( same value should be same obj ) ( cache, control new obj )

from custom_literals import literal


class Kg:
    _kilograms = {} # {1: "1kg obj", 2: "2kg obj"}

    def __new__(cls, n):
        if n in Kg._kilograms:
            return cls._kilograms[n]
        kg = super().__new__(cls) # create new kg
        kg.n = n
        cls._kilograms[n] = kg
        return kg

    def __add__(self, other):
        if type(other) is Kg:
            return Kg(self.n + other.n)
        elif type(other) is Lb:
            return Kg(self.n + other.n / 2.2)

    def __sub__(self, other):
        if type(other) is Kg:
            return Kg(self.n - other.n)
        elif type(other) is Lb:
            return Kg(self.n - other.n / 2.2)

    def __eq__(self, other):
        if type(other) is Kg:
            return self.n == other.n
        elif type(other) is Lb:
            return self.n == other.n / 2.2

    def __repr__(self):
        return f"{self.n}kg"


class Lb:
    cache = {}

    def __new__(cls, n):
        if n in cls.cache:
            return cls.cache[n]
        lb = super().__new__(cls)  # create new lb
        lb.n = n
        cls.cache[n] = lb
        return lb

    def __add__(self, other):
        if type(other) is Lb:
            return Lb(self.n + other.n)
        elif type(other) is Kg:
            return Lb(self.n + other.n * 2.2)

    def __sub__(self, other):
        if type(other) is Lb:
            return Lb(self.n - other.n)
        elif type(other) is Kg:
            return Lb(self.n - other.n * 2.2)

    def __eq__(self, other):
        if type(other) is Lb:
            return self.n == other.n
        elif type(other) is Kg:
            return self.n == other.n * 2.2

    def __repr__(self):
        return f"{self.n}lb"


@literal(int, float, name="kg")
def f1(n):
    return Kg(n)

@literal(int, float, name="lb")
def f2(n):
    return Lb(n)

x = 1 .lb  
y = 1 .lb   
print(id(x))
print(id(y))
print(x is y)

################################################################################################

"""


