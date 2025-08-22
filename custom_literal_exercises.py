"""
# custom data type 

magic method အတွက် exercise ပါ။

#################################################

# step.1 ( draw Kg Type )

class Kg:
    def __init__(self, n):
        self.n = n

    def add(self, other):
        return  self + other

#################################################

# step.2 ( repr )

class Kg:
    def __init__(self, n):
        self.n = n

    def add(self, other):
        return  self + other

    def __repr__(self):
        return f"{self.n} Kg"

#################################################

# step.3 ( +  __add__ )

class Kg:
    def __init__(self, n):
        self.n = n

    def __add__(self, other):
        return  self + other

    def __repr__(self):
        return f"{self.n} Kg"

#################################################

# step.4 ( Lb )

class Lb:
    def __init__(self, n):
        self.n = n

    def __add__(self, other):
        return  self + other

    def __repr__(self):
        return f"{self.n} Lb"

#################################################

# step.5 ( add --> kg , lb )

class Kg:
    def __init__(self, n):
        self.n = n

    def __add__(self, other):
        if type(other) is Kg :
            ans= self.n + other.n
        if type(other) is Lb:
            ans = self.n + other.n / 2.2
        ans = round(ans, 2)
        return Kg(ans)

    def __repr__(self):
        return f"{self.n} Kg"


class Lb:
    def __init__(self, n):
        self.n = n

    def __add__(self, other):
        if type(other) is Lb:
            return Lb(round(self.n + other.n, 2))
        else:
            return Lb(round(self.n + other.n * 2.2, 2))

    def __repr__(self):
        return f"{self.n} Lb"

#################################################

# step.6 ( sub --> kg , lb )


class Kg:
    def __init__(self, n):
        self.n = n

    def __add__(self, other):
        if type(other) is Kg :
            ans= self.n + other.n
        if type(other) is Lb:
            ans = self.n + other.n / 2.2
        ans = round(ans, 2)
        return Kg(ans)

    def __sub__(self, other):
        if type(other) is Kg:
            ans = self.n - other.n
        if type(other) is Lb:
            ans = self.n - other.n / 2.2
        ans = round(ans, 2)
        return Kg(ans)

    def __repr__(self):
        return f"{self.n} Kg"


class Lb:
    def __init__(self, n):
        self.n = n

    def __add__(self, other):
        if type(other) is Lb:
            return Lb(round(self.n + other.n, 2))
        else:
            return Lb(round(self.n + other.n * 2.2, 2))

    def __sub__(self, other):
        if type(other) is Lb:
            return Lb(round(self.n - other.n, 2))
        else:
            return Lb(round(self.n - other.n * 2.2, 2))

    def __repr__(self):
        return f"{self.n} Lb"

#################################################

# step.7 ( literal )

from custom_literals import literal


class Kg:
    def __init__(self, n):
        self.n = n

    def __add__(self, other):
        if type(other) is Kg :
            ans= self.n + other.n
        if type(other) is Lb:
            ans = self.n + other.n / 2.2
        ans = round(ans, 2)
        return Kg(ans)

    def __sub__(self, other):
        if type(other) is Kg:
            ans = self.n - other.n
        if type(other) is Lb:
            ans = self.n - other.n / 2.2
        ans = round(ans, 2)
        return Kg(ans)

    def __repr__(self):
        return f"{self.n} Kg"


class Lb:
    def __init__(self, n):
        self.n = n

    def __add__(self, other):
        if type(other) is Lb:
            return Lb(round(self.n + other.n, 2))
        else:
            return Lb(round(self.n + other.n * 2.2, 2))

    def __sub__(self, other):
        if type(other) is Lb:
            return Lb(round(self.n - other.n, 2))
        else:
            return Lb(round(self.n - other.n * 2.2, 2))

    def __repr__(self):
        return f"{self.n} Lb"


@literal(int, float, name="Kg")
def x(n):
    return Kg(n)


@literal(int, float, name="lb")
def x(n):
    return Lb(n)


print(1 + 2) # 3
print(1 .Kg + 2.2 .lb) # 2.0 Kg
print(2.2 .lb + 1 .Kg) # 4.4 Lb

#################################################

# check eq (error)
print(1 == 1) # True
print(1 .Kg == 1 .Kg) # False

#################################################

# step.8 ( eq )

from custom_literals import literal


class Kg:
    def __init__(self, n):
        self.n = n

    def __add__(self, other):
        if type(other) is Kg :
            ans= self.n + other.n
        if type(other) is Lb:
            ans = self.n + other.n / 2.2
        ans = round(ans, 2)
        return Kg(ans)

    def __sub__(self, other):
        if type(other) is Kg:
            ans = self.n - other.n
        if type(other) is Lb:
            ans = self.n - other.n / 2.2
        ans = round(ans, 2)
        return Kg(ans)

    def __eq__(self, other):
        return self.n == other.n

    def __repr__(self):
        return f"{self.n} Kg"


class Lb:
    def __init__(self, n):
        self.n = n

    def __add__(self, other):
        if type(other) is Lb:
            return Lb(round(self.n + other.n, 2))
        else:
            return Lb(round(self.n + other.n * 2.2, 2))

    def __sub__(self, other):
        if type(other) is Lb:
            return Lb(round(self.n - other.n, 2))
        else:
            return Lb(round(self.n - other.n * 2.2, 2))

    def __eq__(self, other):
        return self.n == other.n

    def __repr__(self):
        return f"{self.n} Lb"


@literal(int, float, name="Kg")
def x(n):
    return Kg(n)


@literal(int, float, name="lb")
def x(n):
    return Lb(n)


# check eq of Kg and Kg( Ok )
print(1 == 1) # True
print(1 .Kg == 1 .Kg) # True

#################################################

# check eq of Kg and Lb( not Ok )
print(1 == 1) # True
print(1 .Kg == 2.2 .lb) # False

#################################################

# step.9 ( eq of Kg and Lb )

from custom_literals import literal


class Kg:
    def __init__(self, n):
        self.n = n

    def __add__(self, other):
        if type(other) is Kg :
            ans= self.n + other.n
        if type(other) is Lb:
            ans = self.n + other.n / 2.2
        ans = round(ans, 2)
        return Kg(ans)

    def __sub__(self, other):
        if type(other) is Kg:
            ans = self.n - other.n
        if type(other) is Lb:
            ans = self.n - other.n / 2.2
        ans = round(ans, 2)
        return Kg(ans)

    def __eq__(self, other):
        if type(other) is Kg:
            return self.n == other.n
        if type(other) is Lb:
            return self.n == other.n / 2.2

    def __repr__(self):
        return f"{self.n} Kg"


class Lb:
    def __init__(self, n):
        self.n = n

    def __add__(self, other):
        if type(other) is Lb:
            return Lb(round(self.n + other.n, 2))
        else:
            return Lb(round(self.n + other.n * 2.2, 2))

    def __sub__(self, other):
        if type(other) is Lb:
            return Lb(round(self.n - other.n, 2))
        else:
            return Lb(round(self.n - other.n * 2.2, 2))

    def __eq__(self, other):
        if type(other) is Lb:
            return self.n == other.n
        if type(other) is Kg:
            return self.n == other.n * 2.2

    def __repr__(self):
        return f"{self.n} Lb"


@literal(int, float, name="Kg")
def x(n):
    return Kg(n)


@literal(int, float, name="lb")
def x(n):
    return Lb(n)


# check eq of Kg and Lb( Ok )
print(1 == 1.0) # True
print(1 .Kg == 2.2 .lb) # True
print(2.2 .lb == 1 .Kg) # True

#################################################

# step.10 (same values should be same object) (cache of kilograms, controlling new obj)

from custom_literals import literal


class Kg:
    _kilograms = {}

    def __new__(cls, n):
        if n in cls._kilograms:
            return cls._kilograms[n]
        kg = super().__new__(cls) # new kg obj from parent
        kg.n = n
        cls._kilograms[n] = kg
        return kg

    def __add__(self, other):
        if type(other) is Kg :
            ans= self.n + other.n
        if type(other) is Lb:
            ans = self.n + other.n / 2.2
        ans = round(ans, 2)
        return Kg(ans)

    def __sub__(self, other):
        if type(other) is Kg:
            ans = self.n - other.n
        if type(other) is Lb:
            ans = self.n - other.n / 2.2
        ans = round(ans, 2)
        return Kg(ans)

    def __eq__(self, other):
        if type(other) is Kg:
            return self.n == other.n
        if type(other) is Lb:
            return self.n == other.n / 2.2

    def __repr__(self):
        return f"{self.n} Kg"


class Lb:
    def __init__(self, n):
        self.n = n

    def __add__(self, other):
        if type(other) is Lb:
            return Lb(round(self.n + other.n, 2))
        else:
            return Lb(round(self.n + other.n * 2.2, 2))

    def __sub__(self, other):
        if type(other) is Lb:
            return Lb(round(self.n - other.n, 2))
        else:
            return Lb(round(self.n - other.n * 2.2, 2))

    def __eq__(self, other):
        if type(other) is Lb:
            return self.n == other.n
        if type(other) is Kg:
            return self.n == other.n * 2.2

    def __repr__(self):
        return f"{self.n} Lb"


@literal(int, float, name="Kg")
def x(n):
    return Kg(n)


@literal(int, float, name="lb")
def x(n):
    return Lb(n)


# check id of same value Kg( Ok )
x = 1 # small int
y = 1
print(x is y) # True

a = 1 .Kg
b = 1 .Kg
print(a is b) # True

#################################################

# same value, same obj (same memory address)(same id)
print(hex(id(a)))
print(hex(id(b)))

# 0x10066c830
# 0x10066c830

#################################################

# different values, different objs (True)
a = 1 .Kg
a = 2 .Kg
print(a is b) # False

#################################################

# check immutable ( not Ok )
a = 1 .Kg
b = 1 .Kg
a.n = 2 # mutable
print(a) # 2 Kg
print(b) # 2 Kg

#################################################

# step.11 (immutable value) (control old attr with original setattr) (use parent setattr for new attr)

from custom_literals import literal


class Kg:
    _kilograms = {}

    def __new__(cls, n):
        if n in cls._kilograms:
            return cls._kilograms[n]
        kg = super().__new__(cls) # new kg obj from parent
        kg.n = n
        cls._kilograms[n] = kg
        return kg

    def __setattr__(self, key, value):
        if hasattr(self, key):
            raise AttributeError("Immutable obj")
        super().__setattr__(key, value)

    def __add__(self, other):
        if type(other) is Kg :
            ans= self.n + other.n
        if type(other) is Lb:
            ans = self.n + other.n / 2.2
        ans = round(ans, 2)
        return Kg(ans)

    def __sub__(self, other):
        if type(other) is Kg:
            ans = self.n - other.n
        if type(other) is Lb:
            ans = self.n - other.n / 2.2
        ans = round(ans, 2)
        return Kg(ans)

    def __eq__(self, other):
        if type(other) is Kg:
            return self.n == other.n
        if type(other) is Lb:
            return self.n == other.n / 2.2

    def __repr__(self):
        return f"{self.n} Kg"


class Lb:
    def __init__(self, n):
        self.n = n

    def __add__(self, other):
        if type(other) is Lb:
            return Lb(round(self.n + other.n, 2))
        else:
            return Lb(round(self.n + other.n * 2.2, 2))

    def __sub__(self, other):
        if type(other) is Lb:
            return Lb(round(self.n - other.n, 2))
        else:
            return Lb(round(self.n - other.n * 2.2, 2))

    def __eq__(self, other):
        if type(other) is Lb:
            return self.n == other.n
        if type(other) is Kg:
            return self.n == other.n * 2.2

    def __repr__(self):
        return f"{self.n} Lb"


@literal(int, float, name="Kg")
def x(n):
    return Kg(n)


@literal(int, float, name="lb")
def x(n):
    return Lb(n)


# check immutable (Ok)
a = 1 .Kg
b = 1 .Kg
a.n = 2 # AttributeError: Immutable obj
print(a)
print(b)

#################################################

#################################################

#################################################

"""