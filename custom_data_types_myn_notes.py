

"""

Custom data types

class    -  Dollar
data     -  n
methods  -  add()

#################################################

ဘယ်လိုရေးတယ်ဆိုတာက Attributes exercises မှာ လေ့ကျင့်ရပါမယ်။

Custom data types မှာတော့ အခုရေးပေးထားတာကို နားလည်ရင် ရပါပြီ။

#################################################

Step.1 
Dollar ဆိုတဲ့ class ဒီဇိုင်းဆွဲတာပါ။

Step.2 
ကိုယ်စားပြုမယ့်စာတန်ဖိုးကို 1 dollar လို့ ပေးချင်တာပါ။

Step.3 
သင်္ကေတနဲ့ ပေါင်းချင်တာပါ။ 

Step.4 
Dollar နှစ်ခုပေါင်းတဲ့အခါ ရလဒ်ကို dollar အဖြစ်နဲ့ပဲ လိုချင်တာပါ။

Step.5 
Kyat ဆိုတဲ့ class ဒီဇိုင်းဆွဲတာပါ။

Step.6 
dollar နဲ့ kyats လိုမျိုး အမျိုးအစား မတူတာတွေကို မှန်မှန်ကန်ကန် ပေါင်းချင်တာပါ။

Step.7 
သင်္ကေတနဲ့ နှုတ်ချင်တာပါ။

Step.8 
သင်္ကေတနဲ့ object ဖန်တီးချင်တာပါ။ 

Step.9
သင်္ကေတနဲ့ တန်ဖိုးတူလား နှိုင်းယှဉ်ချင်တာပါ။

Step.10
dollar နဲ့ kyats လိုမျိုး အမျိုးအစား မတူတာတွေကို မှန်မှန်ကန်ကန် နှိုင်းယှဉ်ချင်တာပါ။

Step.11
Memory သက်သာအောင် တန်ဖိုးတူခဲ့ရင် တစ်ကြိမ်ပဲ ဖန်တီးပြီး ဝေမျှသုံးစေချင်တာပါ။

3 min

#################################################

Step.1 (Draw Dollar Type)

Dollar ဆိုတဲ့ class ဒီဇိုင်းဆွဲတာပါ။


class Dollar:
    def __init__(self, n):
        self.n = n

    def add(self, other):
        return self.n + other.n


x = Dollar(1)
print(x)
print(x.n)


y = Dollar(2)
print(y)
print(y.n)


ans = x.add(y)
print(ans)

#################################################

Step.2 (Representation string -> "1 dollar") 

ကိုယ်စားပြုမယ့်စာတန်ဖိုးကို 1 dollar လို့ ပေးချင်တာပါ။


class Dollar:
    def __init__(self, n):
        self.n = n

    def add(self, other):
        return self.n + other.n

    def __repr__(self):
        return f"{self.n} dollar"


x = Dollar(1)
print(x)


#################################################

Step.3 ( + ) (__add__) 

သင်္ကေတနဲ့ ပေါင်းချင်တာပါ။


class Dollar:
    def __init__(self, n):
        self.n = n

    def __add__(self, other):
        return self.n + other.n

    def __repr__(self):
        return f"{self.n} dollar"


x = Dollar(1)
y = Dollar(2)

ans = x.__add__(y)
print(ans)


ans = x + y
print(ans)

#################################################

Step.4 (result of addition => 3 dollar ) 

Dollar နှစ်ခုပေါင်းတဲ့အခါ ရလဒ်ကို dollar အဖြစ်နဲ့ပဲ လိုချင်တာပါ။

>> Dollar(self.n + other.n)

#################################################


class Dollar:
    def __init__(self, n):
        self.n = n

    def __add__(self, other):
        return Dollar(self.n + other.n)

    def __repr__(self):
        return f"{self.n} dollar"


x = Dollar(1)
y = Dollar(2)
ans = x + y
print(ans)

#################################################

Step.5 ( Design for Kyat )

Kyat ဆိုတဲ့ class ဒီဇိုင်းဆွဲတာပါ။

5000 kyats + 10000 kyats  = 15000 kyats


class Kyat:
    def __init__(self, n):
        self.n = n

    def __add__(self, other):
        return Kyat(self.n + other.n)

    def __repr__(self):
        return f"{self.n} kyat"


x = Dollar(1)
y = Kyat(10000)
ans = x + y
print(ans)


#################################################

Step.6 (dollar + kyats)

dollar နဲ့ kyats လိုမျိုး အမျိုးအစား မတူတာတွေကို မှန်မှန်ကန်ကန် ပေါင်းချင်တာပါ။

1 dollar + 10000 kyats => 3 dollar
10000 kyats + 1 dollar => 15000 kyats

#################################################

if type(other) == Dollar:
    return Dollar(self.n + other.n)
if type(y) == Kyat:
    return Dollar(self.n + other.n / 5000)

#################################################


class Dollar:
    def __init__(self, n):
        self.n = n

    def __add__(self, other):
        if type(other) is Dollar:
            return Dollar(self.n + other.n)
        elif type(other) is Kyat:
            return Dollar(self.n + other.n / 5000)

    def __repr__(self):
        return f"{self.n} dollar"


class Kyat:
    def __init__(self, n):
        self.n = n

    def __add__(self, other):
        if type(other) is Kyat:
            return Kyat(self.n + other.n)
        elif type(other) is Dollar:
            return Kyat(self.n + other.n * 5000)

    def __repr__(self):
        return f"{self.n} kyat"


x = Dollar(1)
y = Kyat(10000)

ans = x + y
print(ans)

ans = y + x
print(ans)

#################################################

1 dollar + 2 dollar      => 3 dollar
a = Dollar(1)
b = Dollar(2)
print(a + b)

10000 kyats + 5000 kyats => 15000 kyats
x = Kyat(5000)
y = Kyat(10000)
print(x + y)

1 dollar + 10000 kyats => 3 dollar
print(a + y)

10000 kyats + 1 dollar => 15000 kyats
print(y + a)

#################################################

Step.7 ( - ) ( __sub__ )

သင်္ကေတနဲ့ နှုတ်ချင်တာပါ။


class Dollar:
    def __init__(self, n):
        self.n = n

    def __add__(self, other):
        if type(other) is Dollar:
            return Dollar(self.n + other.n)
        elif type(other) is Kyat:
            return Dollar(self.n + other.n / 5000)

    def __sub__(self, other):
        if type(other) is Dollar:
            return Dollar(self.n - other.n)
        elif type(other) is Kyat:
            return Dollar(self.n - other.n / 5000)

    def __repr__(self):
        return f"{self.n} dollar"


class Kyat:
    def __init__(self, n):
        self.n = n

    def __add__(self, other):
        if type(other) is Kyat:
            return Kyat(self.n + other.n)
        elif type(other) is Dollar:
            return Kyat(self.n + other.n * 5000)

    def __sub__(self, other):
        if type(other) is Kyat:
            return Kyat(self.n - other.n)
        elif type(other) is Dollar:
            return Kyat(self.n - other.n * 5000)

    def __repr__(self):
        return f"{self.n} kyat"

a = Dollar(1)
b = Dollar(2)
print(b - a)  # 1 d

x = Kyat(5000)
y = Kyat(10000)
print(y - x) # 5000 k

print(a - y) # 1$ - 10000 k = 1 - 2 = -1$
print(y - a) # 10000 k - 1$ = 10000 - 5000 = 5000 k

#################################################

Step.8 (literal)

သင်္ကေတနဲ့ object ဖန်တီးချင်တာပါ။

Create by name 
=> int(1), str(1), Dollar(1)

Create by symbol(literal) 
=> 1, "1", 1 dollar

#################################################

literal
x = 1
y = 1 .dollar

#################################################

Install external pakage
1. custom-literals
2. forbiddenfruit

from custom_literals import literal

@literal(int, float, name="dollar")
def f1(n):
    return Dollar(n)
    

#################################################


from custom_literals import literal


class Dollar:
    def __init__(self, n):
        self.n = n

    def __add__(self, other):
        if type(other) is Dollar:
            return Dollar(self.n + other.n)
        elif type(other) is Kyat:
            return Dollar(self.n + other.n / 5000)

    def __sub__(self, other):
        if type(other) is Dollar:
            return Dollar(self.n - other.n)
        elif type(other) is Kyat:
            return Dollar(self.n - other.n / 5000)

    def __repr__(self):
        return f"{self.n} dollar"


class Kyat:
    def __init__(self, n):
        self.n = n

    def __add__(self, other):
        if type(other) is Kyat:
            return Kyat(self.n + other.n)
        elif type(other) is Dollar:
            return Kyat(self.n + other.n * 5000)

    def __sub__(self, other):
        if type(other) is Kyat:
            return Kyat(self.n - other.n)
        elif type(other) is Dollar:
            return Kyat(self.n - other.n * 5000)

    def __repr__(self):
        return f"{self.n} kyat"



@literal(int, float, name="dollar")
def f1(n):
    return Dollar(n)


@literal(int, float, name="kyat")
def f2(n):
    return Kyat(n)


print(Dollar(1).__add__(Dollar(2)))
print(1 .dollar + 2 .dollar)
print(10000 .kyat + 5000 .kyat)
print(1 .dollar + 10000 .kyat)
print(10000 .kyat + 1 .dollar)

#################################################

Step.9 ( == ) ( __eq__ ) 

သင်္ကေတနဲ့ တန်ဖိုးတူလား နှိုင်းယှဉ်ချင်တာပါ။

== (equal to, equality operator)

equal number 

#################################################

from custom_literals import literal


class Dollar:
    def __init__(self, n):
        self.n = n

    def __add__(self, other):
        if type(other) is Dollar:
            return Dollar(self.n + other.n)
        elif type(other) is Kyat:
            return Dollar(self.n + other.n / 5000)

    def __sub__(self, other):
        if type(other) is Dollar:
            return Dollar(self.n - other.n)
        elif type(other) is Kyat:
            return Dollar(self.n - other.n / 5000)

    def __eq__(self, other):
        return self.n == other.n

    def __repr__(self):
        return f"{self.n} dollar"


class Kyat:
    def __init__(self, n):
        self.n = n

    def __add__(self, other):
        if type(other) is Kyat:
            return Kyat(self.n + other.n)
        elif type(other) is Dollar:
            return Kyat(self.n + other.n * 5000)

    def __sub__(self, other):
        if type(other) is Kyat:
            return Kyat(self.n - other.n)
        elif type(other) is Dollar:
            return Kyat(self.n - other.n * 5000)

    def __eq__(self, other):
        return self.n == other.n
        
    def __repr__(self):
        return f"{self.n} kyat"


@literal(int, float, name="dollar")
def f1(n):
    return Dollar(n)


@literal(int, float, name="kyat")
def f2(n):
    return Kyat(n)


print(1 .dollar == 1 .dollar)
print(5000 .kyat == 5000 .kyat)

#################################################

Step.10 ( dollar == kyat )

dollar နဲ့ kyats လိုမျိုး အမျိုးအစား မတူတာတွေကို မှန်မှန်ကန်ကန် နှိုင်းယှဉ်ချင်တာပါ။


from custom_literals import literal


class Dollar:
    def __init__(self, n):
        self.n = n

    def __add__(self, other):
        if type(other) is Dollar:
            return Dollar(self.n + other.n)
        if type(other) is Kyat:
            return Dollar(self.n + other.n / 5000)

    def __sub__(self, other):
        if type(other) is Dollar:
            return Dollar(self.n - other.n)
        if type(other) is Kyat:
            return Dollar(self.n - other.n / 5000)

    def __eq__(self, other):
        if type(other) is Dollar:
            return self.n == other.n
        if type(other) is Kyat:
            return self.n == other.n / 5000

    def __repr__(self):
        return f"{self.n} dollar"


class Kyat:
    def __init__(self, n):
        self.n = n

    def __add__(self, other):
        if type(other) is Kyat:
            return Kyat(self.n + other.n)
        if type(other) is Dollar:
            return Kyat(self.n + other.n * 5000)

    def __sub__(self, other):
        if type(other) is Kyat:
            return Kyat(self.n - other.n)
        if type(other) is Dollar:
            return Kyat(self.n - other.n * 5000)

    def __eq__(self, other):
        if type(other) is Kyat:
            return self.n == other.n
        if type(other) is Dollar:
            return self.n == other.n * 5000

    def __repr__(self):
        return f"{self.n} kyat"


@literal(int, float, name="dollar")
def f1(n):
    return Dollar(n)


@literal(int, float, name="kyat")
def f2(n):
    return Kyat(n)


# print(1 .dollar == 5000 .kyat)
# print(5000 .kyat == 1 .dollar)

x = Dollar(1)    # 4338709616
y = Dollar(1)    # 4338709760
z = Dollar(1)    # 4338978592


print(id(x))
print(id(y))
print(id(z))


#################################################

Step.11

Memory သက်သာအောင် တန်ဖိုးတူခဲ့ရင် တစ်ကြိမ်ပဲ ဖန်တီးပြီး ဝေမျှသုံးစေချင်တာပါ။

x = Dollar(1)    # 4338709616
y = Dollar(1)    # 4338709760
z = Dollar(1)    # 4338978592

x = Dollar(1)    # 4338709616
y = Dollar(1)    #     ... old
z = Dollar(1)    #     ... old

#################################################

if same value, 
1. do not create new obj
2. reuse the old one

x = {1: "apple", 2: "orange"}
x[2]

x.keys() = [1, 2]
x.values() = ["apple", "orange"]

x = {}

x[1] = "apple"
x = {1: "apple"}

x[2] = "orange"
x = {1: "apple", 2: "orange"}

x = {}
x[n] = new
x[1] = 0x100d52120

x = {1: 0x100d52120}

x[1]

#################################################

တန်ဖိုးတူခဲ့ရင် တစ်ကြိမ်ပဲ ဖန်တီး  =>  new()


class Dollar:
    x = {}

    def __new__(cls, n):
        if n in Dollar.x.keys():
            return Dollar.x[n]                # 0x100d52120
        else:
            new = super().__new__(cls)        # 0x100d52120
            new.n = n                         # 0x100d52120 <- n=1
            Dollar.x[n] = new
            return new



x = Dollar(1)    # 0x100d52120
y = Dollar(1)    # 0x100d52120

#################################################

from custom_literals import literal


class Dollar:
    x = {}

    def __new__(cls, n):
        if n in Dollar.x.keys():
            return Dollar.x[n]                # 0x100d52120
        else:
            new = super().__new__(cls)        # 0x100d52120
            new.n = n                         # 0x100d52120 <- n=1
            Dollar.x[n] = new
            return new

    def __add__(self, other):
        if type(other) is Dollar:
            return Dollar(self.n + other.n)
        if type(other) is Kyat:
            return Dollar(self.n + other.n / 5000)

    def __sub__(self, other):
        if type(other) is Dollar:
            return Dollar(self.n - other.n)
        if type(other) is Kyat:
            return Dollar(self.n - other.n / 5000)

    def __eq__(self, other):
        if type(other) is Dollar:
            return self.n == other.n
        if type(other) is Kyat:
            return self.n == other.n / 5000

    def __repr__(self):
        return f"{self.n} dollar"


class Kyat:
    x = {}

    def __new__(cls, n):
        if n in Kyat.x.keys():
            return Kyat.x[n]
        else:
            new = super().__new__(cls)
            new.n = n
            Kyat.x[n] = new
            return new

    def __add__(self, other):
        if type(other) is Kyat:
            return Kyat(self.n + other.n)
        if type(other) is Dollar:
            return Kyat(self.n + other.n * 5000)

    def __sub__(self, other):
        if type(other) is Kyat:
            return Kyat(self.n - other.n)
        if type(other) is Dollar:
            return Kyat(self.n - other.n * 5000)

    def __eq__(self, other):
        if type(other) is Kyat:
            return self.n == other.n
        if type(other) is Dollar:
            return self.n == other.n * 5000

    def __repr__(self):
        return f"{self.n} kyat"


@literal(int, float, name="dollar")
def f1(n):
    return Dollar(n)


@literal(int, float, name="kyat")
def f1(n):
    return Kyat(n)


x = 10000 .kyat 
y = 10000 .kyat 

z = x + y
a = y + x

print(id(x))
print(id(y))
print(id(z))
print(id(a))

##################################################################################################

1 + 2.6

int
1 + 2      =>   3       truncate             =>   return self.n + int(other)
1 + 3      =>   4       round                =>   return self.n + round(other)

float
1.0 + 2.6  =>   3.6                           =>   return float(self.n) + other

##################################################################################################


class Myint(int):
    def __init__(self, n):
        self.n = n

    def __add__(self, other):
        if type(other) is int:
            return self.n + other
        if type(other) is float:
            return self.n + round(other)


x = int(1)
y = 2.6
print(x + y)

x = Myint(1)
y = 2.6
print(x + y)

##################################################################################################

Share Vs New

28 bytes Vs 28 million bytes

##################################################################################################

"""