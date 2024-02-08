

# instruction ( one ins in one line, semicolon )
# translate ( top to bottom, left to right ) ( override ) ( lifo ) ( stack )
# variable name ( value ) ( data type )
# function ( effect, result )

# OOP ( object oriented programming )
# class ( blueprint of object ) ( data + function )
# obj, instance  ( name, attribute data, method ) ( constructor , magic method, normal method )


# attributes ( class, object ) ( dot notation ) ( getattr and setatr(=) )
# variable attribute ( data )
# methods attribute ( function ) ( magic method, normal method )

# type function  1 argv  --> to check type                    ---> type(x), type(type(x)), type(int)  ( Everything become from type. )
#                3 argvs --> to creat a type , model, class   ---> type("A", (), {"a": 123})
#

# OOP, class, object, attributes ( data, method )
# built-in type ( int, str, list, set, .... )
# custom-type ( class keyword, type() ) ( creating a new type, new model & new class)

#########################################

# name, data, method

#########################################

# Computer,
# serial_number, color,
# on, off


"""
class Computer:
    count = 0
    def __init__(self):
        Computer.count += 1
        self.serial_number = "Dell_000" + str(Computer.count)
        self.color = "black" if Computer.count % 2 != 0 else "white"

    def on(self):
        print(f"Computer {self.serial_number} power on.")

    def off(self):
        print(f"Computer {self.serial_number} power off.")

    def __str__(self):
        return f"No = {self.serial_number}\nColor = {self.color}\n"

    def __mod__(self, other):
        return "abc"



computers = []
for i in range(1000):
    computers.append(Computer())

print(computers[0] % computers[1])


for computer in computers:
    computer.on()

for computer in computers:
    computer.off()

#########################################

# name = Car
# data = engine, brake
# method = make_brake, start, stop


class Car:
    def __init__(self, engine, brake):
        self.engine = engine
        self.brake = brake
        self.engine_state = "off"

    def start(self):
        self.engine_state = "on"
        print(f"{self.engine} start.")

    def stop(self):
        self.engine_state = "off"
        print(f"{self.engine} stop.")

    def make_brake(self):
        print(f"{self.brake} braked.")

c1 = Car("diesel engine", "Hydraulic brake")

print(c1.__dict__)
c1.start()
print(c1.__dict__)
c1.stop()
print(c1.__dict__)

#########################################

# name = Robot
# data = fan, motor
# method = autofly , fly, land

class Robot:
    def __init__(self, fan, motor):
        self.fan = fan
        self.motor = motor

    def autofly(self):
        print("auto fly.")

    def fly(self):
        print("fly")

    def land(self):
        print("landing")

"""
#########################################

# 1. inheritance  ( tightly coupled ) ( is a ) ( mg mg is a human. )
# super class, base class,    parent class
# subclass, derived class, child class

# 2. composition ( loosely coupled ) ( friendship ) ( has a ) ( mg mg has a head. )
# 3. tightly coupled & loosely coupled
# 4. "is a" relationship & "has a" relationship
# 5. LIFO ( last in first out )

#########################################

#                                    object
#                                  /        \

#                       live obj                unlived obj

#
#                    /            \

#            human                     animals

#         /          \

#     male              female



#    /  \                      \
# mg mg  aung aung               ma ma


# super class  of mg mg ---> male, human, live obj, obj
# super class of ma ma  ---> female, human, live obj, obj

# super class of live obj ---> obj
# sub class of live obj ---> human, animals, male, female

#########################################

# 1. create class A
# 2. B and C are sub/child/derived classes of A.
# 3. D and E are sub/child/derived classes of B.
# 4. F AND G are sub/child/derived classes of C.

# 5. Z is sub class of D, E , F, G.

#########################################

#           A

#      /        \
#    B           C
#  /   \       /   \
# D     E     F     G
#   \    \   /    /

#          Z
"""

class A:
    pass

class B(A):
    pass
class C(A):
    pass

class D(B):
    pass
class E(B):
    pass

class F(C):
    pass
class G(C):
    pass

class Z(D, E, F, G):
    pass

print(Z.__mro__)


#  Z DEB FGC A
(<class '__main__.Z'>,

<class '__main__.D'>,
<class '__main__.E'>,
<class '__main__.B'>,

<class '__main__.F'>,
<class '__main__.G'>,
<class '__main__.C'>,

<class '__main__.A'>,

<class 'object'>)

###########
"""

#           A

#      /        \
#    B           C
#  /   \       /   \
# D     E     F     G
#        \   /

#          Z

"""
(<class '__main__.Z'>, 

<class '__main__.E'>, 
<class '__main__.B'>, 

<class '__main__.F'>, 
<class '__main__.C'>, 

<class '__main__.A'>, 

<class 'object'>)
"""

#########################################

#########################################

# LIFO
# A   B   C
#  Z D  E  B F G C A



#           A

#      /        \
#    B           C
#  /   \       /   \
# D     E     F     G
#   \    \   /    /

#          Z


#    A

#    C
#  /   \
# F     G
#  \   /
#    Z

#    B
#  /   \
# D     E
#  \   /
#    Z

"""
class Z(D, E, F, G):
    pass
    #x = "x of Z"

print(Z.x)

"""
####################

# multiple inheritance

# Z is sub class of D, E , F, G.

# D     E     F     G
#   \    \   /    /

#          Z

"""
class D():
    pass
    #x = "x of D"
class E():
    pass
    #x = "x of E"
class F():
    pass
    #x = "x of F"
class G():
    x = "x of G"


class Z(D, E, F, G):
    pass
    #x = "x of Z"

print(Z.x)

####################

"""

# Example code of inheritance ( tightly coupled ) ( is a relationships )
# GasEngineCar is a car.
# DieselEngineCar is a car.
#      car
#     /       \
# gas car       diesel car

"""
class Car:
    def __init__(self, engine):
        pass

class GasEngineCar(Car):
    def __init__(self, horse_power):
        self.hp = horse_power

    def start(self):
        print('Starting {}hp gas engine'.format(self.hp))

class DieselEngineCar(Car):
    def __init__(self, horse_power):
        self.hp = horse_power

    def start(self):
        print('Starting {}hp diesel engine'.format(self.hp))

my_car = GasEngineCar(4)
my_car.start()
print()
my_car2 = DieselEngineCar(2)
my_car2.start()
print()


####################


# composition ( loosely coupled ) ( has a relationships )
# car has a engine.
# gas , diesel, petro

class GasEngine:
    def __init__(self, horse_power):
        self.hp = horse_power

    def start(self):
        print('Starting {}hp gas engine'.format(self.hp))

class DieselEngine:
    def __init__(self, horse_power):
        self.hp = horse_power

    def start(self):
        print('Starting {}hp diesel engine'.format(self.hp))

class ABS_brake:
    def brake(self):
        print("safty break with ABS system.")


class Car:
    def __init__(self, engine, brake_system):
        self.engine = engine # composition / has a / cas has an engine
        self.brake_system = brake_system # car has a brake

my_car = Car(GasEngine(4), ABS_brake())
my_car.engine.start()
my_car.brake_system.brake()
print()

my_car2 = Car(DieselEngine(2), ABS_brake())
my_car2.engine.start()
my_car2.brake_system.brake()
print()

my_car2.engine = GasEngine(10)
my_car2.engine.start()
print()

#################################################

# attributes --> class, obj
# data, methods

#################################################

# (count, serial_No, color, state) ( serial(), on(), off() )

# count, serial_No, color, state
# class data = count
# obj data = serial_No, color, state ( automatic )

# serial(), on(), off()
# class method = serial() # auto define serial numbers
# obj method = on(), off()

# private ( data, method )
# double underscoll  (add "_class name" to variable )
# single underscoll  ( normal variable name) ( notic )
# private access --> access from method
# assign / change new value --> change from method
# delete ---> delete from methods

# attribute check --> __dict__, hasattr(obj, "name")  eg . hasattr(c, "window_version")

# underscoll lesson

# cls data Vs obj data
# common data ( cls data / all obj data )
# obj data

#################################################

Attributes exercises

1. Laptop တွင် serial_no ပါသည်။ on, off လုပ်နိုင်သည်။

Note

a.  name --> Laptop
b.  attributes
data --> serial_no
method --> on, off

class Laptop:
    def __init__(self, serial_no):
        self.serial_no = serial_no
    def on(self):
        print("power on")
    def off(self):
        print("power off")

#################################################

2.  Network_Card တွင် speed ပါသည်။ သတ်မှတ် speed ဖြင့် download ဆွဲနိုင်သည်။

a.  name --> Network_Card
b.  attributes
data --> speed
method --> download

class Network_Card:
    def __init__(self, speed):
        self.speed = speed
    def download(self):
        print(f"download with speed {self.speed}")

#################################################

3. 1995 တွင် ပေါ်ပေါက်ခဲ့သော DialUp ဟူသော network card အမျိုးအစား၏ download ဆွဲနိုင်သော အမြန်နှုန်း speed သည် 9600bit/s ဖြစ်သည်။
ထိုအမြန်နှုန်းဖြင့် download ဆွဲနိုင်သည်။

a.  name --> DialUp
b.  attributes
data --> speed = 9600bit/s
method --> download

class DialUp:
    def __init__(self):
        self.speed = "9600bit/s"
    def download(self):
        print(f"download with speed {self.speed}")

#################################################

4. 1999 တွင် ပေါ်ပေါက်ခဲ့သော ADSL ဟူသော network card အမျိုးအစား၏ download ဆွဲနိုင်သော အမြန်နှုန်း speed သည် 2000000bit/s (2Mbit/s)  ဖြစ်သည်။
ထိုအမြန်နှုန်းဖြင့် download ဆွဲနိုင်သည်။

a.  name --> ADSL
b.  attributes
data --> speed = 2000000bit/s
method --> download

class ADSL:
    def __init__(self):
        self.speed = "2000000bit/s"
    def download(self):
        print(f"download with speed {self.speed}")

#################################################

5. 2006 တွင် ပေါ်ပေါက်ခဲ့သော Ethernet ဟူသော network card အမျိုးအစား၏ download ဆွဲနိုင်သော အမြန်နှုန်း speed သည် 10Mbit/s  ဖြစ်သည်။
ထိုအမြန်နှုန်းဖြင့် download ဆွဲနိုင်သည်။

a.  name --> ADSL
b.  attributes
data --> speed = 10000000bit/s
method --> download

class Ethernet_2006:
    def __init__(self):
        self.speed = "10000000bit/s"
    def download(self):
        print(f"download with speed {self.speed}")

#################################################

6. 2014 တွင်  Ethernet_2014 ဟူသော network card အမျိုးအစား၏ download ဆွဲနိုင်သော အမြန်နှုန်း speed သည် 10000Mbit/s  ( တစ်စက္ကန့်လျှင် 1250 မီဂါဘိုက်) ဖြစ်သည်။
ထိုအမြန်နှုန်းဖြင့် download ဆွဲနိုင်သည်။

a.  name --> Ethernet_2014
b.  attributes
data --> speed = 10000Mbit/s
method --> download

class Ethernet_2014:
    def __init__(self):
        self.speed = "10000Mbit/s"
    def download(self):
        print(f"download with speed {self.speed}")

#################################################

7. Car မှာ ကားနံပါတ် တာယာနဲ့ အင်ဂျင်ပါတယ်။ (VIN, engine, tires)

a.  name --> Car
b.  attributes
data --> (VIN, engine, tires)
method -->

class Car:
    def __init__(self, VIN, engine, tires):
        self.VIN = VIN
        self.engine = engine
        self.tires = tires

#################################################

8. Tires ( ကားတာယာ ) တွင် size နှင့် pressure ပါသည်။
pressure ၏ မူလတန်ဖိုးသည် 0 ( psi ) ဖြစ်သည်။
လေထိုးသောလုပ်ဆောင်ချက်ပါသည်။ သတ်မှတ်ပေးလိုက်သော ဖိအားအတိုင်း လေထိုးပေးမည်။

a.  name --> Tires
b.  attributes
data --> size, pressure = 0 ( psi )
method --> pump()

class Tires:
    def __init__(self, size, pressure=0):
        self.size = size
        self.pressure = pressure
    def pump(self, pressure):
        self.pressure = pressure
        print(f"pump tires to {self.pressure} psi.")

city_tire = Tires(15)
print(city_tire.size)
print(city_tire.pressure)

city_tire.pump(8)
print(city_tire.pressure)

off_road_tire = Tires(18)
print(off_road_tire.size)
print(off_road_tire.pressure)

off_road_tire.pump(12)
print(off_road_tire.pressure)


( ဗဟုသုတ --> မြို့တွင်းမောင်းသောကားတာယာ၏ size သည် 15 လက်မ ဖြစ်ပြီး လမ်းကြမ်းမောင်းသော ကားတာယာ၏ size သည် 18 လက်မဖြစ်သည်။ )

#################################################

9. Engine တွင် fuel_type ပါသည်။
စက်နှိုး/မနှိုး ဟူသော အခြေအနေ  state ပါသည်။
မူလအခြေအနေမှာ စက်မနှိုးထားသဖြင့် off ဖြစ်နေမည်။
ပေးထားသော fuel_type ဖြင့် စက်နှိုး ၊ စက်ရပ် မည့်လုပ်‌ဆောင်ချက်ပါသည်။ ( on(), off() )

a.  name --> Engine
b.  attributes
data --> fuel_type, state="off"
method --> on(), off()

class Engine:
    def __init__(self, fuel_type, state="off"):
        self.fuel_type = fuel_type
        self.state = state

    def on(self):
        self.state = "on"
        print(f"Engine on with {self.fuel_type} fuel type.")

    def off(self):
        self.state = "off"
        print(f"Engine off with {self.fuel_type} fuel type.")


e1 = Engine("petrol")
print(e1.__dict__)
e1.on()
print(e1.__dict__)
e1.off()
print(e1.__dict__)

#################################################

Combination exercise
10. Car မှာ ကားနံပါတ် တာယာနဲ့ အင်ဂျင်ပါတယ်။ (VIN, engine, tires)
မေးခွန်း နံပါတ် 8 နှင့် 9 တွင် ဖန်တီးခဲ့သော တာယာနှင့် အင်ဂျင်ကို ယူသုံးပြီး city_car တစ်စီးဖန်တီးပါ။
ကားနံပါတ်မှာ 001A ၊ တာယာမှာ 15 လက်မ၊ ဆီအမျိုးအစားမှာ petrol ဓါတ်ဆီ ဖြစ်သည်။
ထိုကားကို လေဖိအား 3 psi ထိလေထိုးပြီး စက်နှိုးပါ။


class Car:
    def __init__(self, VIN, engine, tires):
        self.VIN = VIN
        self.engine = engine
        self.tires = tires

class Tires:
    def __init__(self, size, pressure=0):
        self.size = size
        self.pressure = pressure
    def pump(self, pressure):
        self.pressure = pressure
        print(f"pump tires to {pressure} psi.")


class Engine:
    def __init__(self, fuel_type, state="off"):
        self.fuel_type = fuel_type
        self.state = state

    def on(self):
        self.state = "on"
        print(f"Engine on with {self.fuel_type} fuel type.")

    def off(self):
        self.state = "off"
        print(f"Engine off with {self.fuel_type} fuel type.")

# ကားနံပါတ်မှာ 001A ၊ တာယာမှာ 15 လက်မ၊ ဆီအမျိုးအစားမှာ petrol ဓါတ်ဆီ ဖြစ်သည်။
city_car = Car(VIN="001A", engine=Engine("petrol"), tires=Tires(15))

# ထိုကားကို လေဖိအား 3 psi ထိလေထိုးပြီး စက်နှိုးပါ။
city_car.tires.pump(3)
city_car.engine.on()

#################################################

inheritance exercise

11. Jet လေယာဉ်တွင် တိုက်ခိုက်မှုအမျိုးအစား ၊ အမည်နှင့် ထုတ်လုပ်သောနိုင်ငံဟူသော အချက်အလက်ပါရှိသည်။
( role, name, country )
F35 နှင့် F22 သည် Jet လေယာဉ်ဖြစ်သည်။
       Jet
     /     \
   F35     f22

a.  name --> Jet
b.  attributes
data -->  role, name, country
method -->

class Jet:
    def __init__(self, role, name, country):
        self.role = role
        self.name = name
        self.country = country

# F35 သည် Jet လေယာဉ်ဖြစ်သည်။

class F35(Jet):
    pass

# F22 သည် Jet လေယာဉ်ဖြစ်သည်။
class F22(Jet):
    pass

#################################################

12.
I, J, K သည် A ၏ sub class ဖြစ်သည်။
X သည် I ၏ sub class ဖြစ်သည်။
Y သည် J ၏ sub class ဖြစ်သည်။
Z သည် K ၏ sub class ဖြစ်သည်။
ပုံဆွဲပါ။
class တည်ဆောက်ပါ။

"""
#         A
#      / /  \
#   I   J    K
#  /   /      \
# X   Y        Z


"""
class A:
    pass

class I(A):
    pass
class J(A):
    pass
class K(A):
    pass

class X(I):
    pass

class Y(J):
    pass

class Z(K):
    pass

#################################################

13.  အောက်ပါပုံအတိုင်း class တည်ဆောက်ပါ။

"""
# ................  .Fruit

# .......  ...../. .....\......\

#        Apple        Mango          Banana
#      ............/.. .\   ...\
#          မချစ်စု        စိန်တလုံး    တောသရက်

"""
class Fruit:
    pass

class Apple(Fruit):
    pass
class Mango(Fruit):
    pass
class Banana(Fruit):
    pass

class မချစ်စု(Mango):
    pass
class စိန်တလုံး(Mango):
    pass
class တောသရက်(Mango):
    pass

#################################################

multiple inheritance exercises
14. ပန်းသီးနှင့် သစ်တော်သီးသည် သစ်သီးများဖြစ်ကြသည်။
 ပန်းသစ်တော်သီးသည် ပန်းသီးနှင့် သစ်တော်သီးနှစ်မျိုးလုံးမှ မျိုးဗီဇများ အမွေဆက်ခံထားသည်။
ထို့ကြောင့် ပန်းသစ်တော်သီးသည် ပန်းသီးလည်း ဖြစ်သလို သစ်တော်သီးလည်းဖြစ်သည်။
ပုံဆွဲပြီး class တည်ဆောက်ပါ။
"""
#     Fruit
#  /        \
#apple     သစ်တော်သီး
#  \        /
#  ပန်းသစ်တော်သီး

"""
class Fruit:
    pass
class Apple(Fruit):
    pass
class သစ်တော်သီး(Fruit):
    pass

class ပန်းသစ်တော်သီး(apple, သစ်တော်သီး):
    pass

ပန်းသစ်တော်သီး MRO ---> ပန်းသစ်တော်သီး, apple, သစ်တော်သီး, Fruit

#################################################
"""
# diamond broblem
#        Fruit
#    /   /        \
#   \   apple     သစ်တော်သီး
#    \  \        /
#      ပန်းသစ်တော်သီး

"""

class ပန်းသစ်တော်သီး(Fruit, apple, သစ်တော်သီး): # diamond broblem
    pass
ပန်းသစ်တော်သီး MRO ---> ပန်းသစ်တော်သီး, Fruit,  apple, သစ်တော်သီး, Fruit


class Fruit:
    pass

class apple(Fruit):
    pass
class သစ်တော်သီး(Fruit):
    pass

class ပန်းသစ်တော်သီး(apple, သစ်တော်သီး):
    pass

print(ပန်းသစ်တော်သီး.__mro__)

#################################################

15.
A, B သည် Y ဖြစ်သည်။
C, D, E သည် Z ဖြစ်သည်။
X သည် A, B, C, D, E, F ဖြစ်သည်။
ပုံဆွဲပြီး class တည်ဆောက်ပါ။
"""

#       Y
#     /   \
#    A     B
#
#         Z
#     /  /  \
#    C  D    E
#
#A   B   C   D   E  F
# \  \  \   /  /  /
#   \ \  \ /  /  /
#         X
#
#  Y          Z
#/   \    /  /  \
#A   B   C   D   E   F
# \  \  \   /  /   /
#   \ \  \ /  /  /
#    \ \ \ / / /
#     \ \\ ///
#
#         X

"""
class Y:
    pass

class Z:
    pass

class A(Y):
    pass
class B(Y):
    pass

class C(Z):
    pass
class D(Z):
    pass
class E(Z):
    pass

class F:
    pass

class X(A, B, C, D, E, F):
    pass

print(X.__mro__)


#################################################

16. X ၏ attributes ကို ရှာဖွေပါက မည့်သည့်အစီအစဉ်အတိုင်းရှာဖွေမည်နည်း။
နမူနာ အဖြေ
Method Resolution Order = X -> A  -> B -> C -> D -> E -> F -> Y -> Z

Ans : Method Resolution Order = X ->    A  -> B -> Y ->    C -> D -> E -> Z  ->    F
                                X       A     B    Y       C    D    E    Z        F

#################################################

#################################################

class Engine:
    def __init__(self, fuel):
        self.fuel = fuel
        self.state = "off"

    def start(self):
        self.state = 'on'

    def stop(self):
        self.state = 'off'

    def get_state(self):
        return self.state

    def __str__(self):
        return f"{self.fuel} Engine ({self.state} condition)"

# tire (us)
# tyre (common english)

class Tire:
    def __init__(self, car):
        # different value, different data
        if car == "city car":
            self.tire_name = "city tire"
            self.city_tire_size = 15
        elif car == "off road car":
            self.tire_name = "off road tire"
            self.off_road_tire_size = 18
        else:
            self.tire_name = None
            print(f"We have not tires for {car}.")
        self.pressure = 0

    def get_pressure(self):
        return self.pressure

    def pump(self, psi):
        self.pressure = psi

    def __str__(self):
        if hasattr(self, "city_tire_size"):
            size = self.city_tire_size
        elif hasattr(self, "off_road_tire_size"):
            size = self.off_road_tire_size
        else:
            size = None
        return f"{size} inches {self.tire_name} ({self.pressure} psi)"

class Car:
    n = 0
    def __init__(self, engine, tires):
        self.engine = engine
        self.tires = tires
        Car.n += 1
        self.vin = f"BMW_{Car.n:0>5}"

    def pump(self, psi):
        self.tires.pump(psi)

    def start(self):
        self.engine.start()

    def stop(self):
        self.engine.stop()

    def tire_name(self):
        return self.tires.tire_name

    def __str__(self):
        return f"\nCar No. = {self.vin}\nCar Engine = {self.engine}\nCar Tyres = {self.tires}\n"

    def __repr__(self):
        return self.vin

petrol_engine = Engine("petrol")
diesel_engine = Engine("diesel")

city_tires = Tire("city car")
off_road_tires = Tire("off road car")

city_petrol_car = Car(Engine("petrol"), Tire("city car"))
city_petrol_car.start()

city_petrol_car2 = Car(Engine("petrol"), Tire("city car"))
city_petrol_car2.pump(7)

print(city_petrol_car)
print(city_petrol_car2)

city_petrol_car = Car(Engine("petrol"), Tire("city car"))
off_road_diesel_car = Car(Engine("diesel"), Tire("off road car"))

# call method
city_petrol_car.engine.start()
city_petrol_car.start()

# access data
print(city_petrol_car.tires.tire_name)
print(city_petrol_car.tire_name())

# access difference data of same class
print(city_petrol_car.tires.city_tire_size)
print(off_road_diesel_car.tires.off_road_tire_size)

cars = list()
# creating cars
for i in range(500):
    cars.append(Car(Engine("petrol"), Tire("city car")))
    cars.append(Car(Engine("diesel"), Tire("off road car")))

print(cars[0])# str
print(cars)# repr

# access different data
for car in cars:
    if hasattr(car.tires, "city_tire_size"):
        print(car.tires.city_tire_size)
    elif hasattr(car.tires, "off_road_tire_size"):
        print(car.tires.off_road_tire_size)

# print(cars[0].tires)

cars[3].tires.pump(10)
for car in cars:
    print(car.tires)

for car in cars:
    if car.tires.tire_name == "city tire" and car.tires.pressure != 7:
        car.pump(7)
    elif car.tires.tire_name == "off road tire" and car.tires.pressure != 10:
        car.pump(10)
    car.start()

for car in cars:
    print(car)

#################################################

#################################################

class Tire:
    def __init__(self, car, pressure=0):
        self.pressure = pressure
        if car == "city car":
            self.tire_name = "city tire"
            self.city_tire_size = 15
        elif car == "off road car":
            self.tire_name = "off road tire"
            self.off_road_tire_size = 18
        else:
            print(f"We have not tires for {car}.")

    def pump(self, pressure):
        self.pressure = pressure
        print(f"pump tires to {pressure} psi.")

class Engine:
    def __init__(self, fuel_type, state="off"):
        self.fuel_type = fuel_type
        self.__state = state

    def __on(self): # _Engine__on()
        self.__state = "on"
        print(f"Engine on with {self.fuel_type} fuel type.")

    def __off(self):
        self.__state = "off"
        print(f"Engine off with {self.fuel_type} fuel type.")

    def __str__(self):
        return f"{self.fuel_type} Engine ({self.__state} condition)"

class Car:
    no = 0
    def __init__(self, engine, tires):
        Car.no += 1
        self.VIN = Car.no
        self.engine = engine
        self.tires = tires

    def on(self):
        self.engine._Engine__on()

    def off(self):
        self.engine._Engine__off()

    def pump(self, pressure):
        self.tires.pump(pressure)

    def get_size(self):
        return self.tires.size

cars = list()

for i in range(10):
    cars.append(Car(Engine("petrol"), Tire("city car")))
    cars.append(Car(Engine("diesel"), Tire("off road car")))

for car in cars:
    if hasattr(car.tires, "city_tire_size"):
        print(car.tires.city_tire_size)
    elif hasattr(car.tires, "off_road_tire_size"):
        print(car.tires.off_road_tire_size)

cars[0].on()
print(cars[0].engine)
cars[0].off()
print(cars[0].engine)

#################################################

1. class
Engine , Tyre
Car has Engine and Tyre

#################################################

2. if we use combination method, we need to take care not to use same obj

#################################################

3. call method / access data

city_petrol_car.engine.start()
print(city_petrol_car.tires.size)

#################################################

4. same attribute with different value
        if car == "city car":
            self.size = 15
        elif car == "off road car":
            self.size = 18
        else:
            self.size = None
            print(f"We have not tires for {car}.")

#city_tires = Tire("city car")
#off_road_tires = Tire("off road car")
#snow_tires = Tire("snow car")

#################################################

5. name space
# call method
city_petrol_car.engine.start()
city_petrol_car.start()

# access data
print(city_petrol_car.tires.size)
print(city_petrol_car.get_size())

#################################################

6. private access
( engine ကတစ်ဆင့် စက်နှိုးခွင့်မပေး ) ( __start() )
( ကားကတစ်ဆင့် စက်နှိုးခွင့်ပေး )
def start(self):
        self.engine._Engine__start()

#city_petrol_car.engine.start()
city_petrol_car.start()

#################################################

7. different value, different data
        if car == "city car":
            self.tire_name = "city tire"
            self.city_tire_size = 15
        elif car == "off road car":
            self.tire_name = "off road tire"
            self.off_road_tire_size = 18
        else:
            print(f"We have not tires for {car}.")

#################################################

8. access difference data of same class

print(city_petrol_car.tires.city_tire_size)
print(off_road_diesel_car.tires.off_road_tire_size)

cars = list()

for i in range(10):
    cars.append(Car(Engine("petrol"), Tire("city car")))
    cars.append(Car(Engine("diesel"), Tire("off road car")))

for car in cars:
    if hasattr(car.tires, "city_tire_size"):
        print(car.tires.city_tire_size)
    elif hasattr(car.tires, "off_road_tire_size"):
        print(car.tires.off_road_tire_size)

#################################################

9. adding obj methods

#################################################

10. adding magic method
def __str__(self):
       return f"\nCar No. = {self.vin}\nCar Engine = {self.engine}\nCar Tyres = {self.tires}\n"

#print(cars[0].tires)
for car in cars:
    print(car.tires)

for car in cars:
    print(car)

#################################################

OOP  ---> object ( variable, methods )

Major OOP Concepts
# 1. polymorphism
# 2. inheritance
# 3. encapsulation ( data hiding )
# 4. abstraction

#################################################

# 1. polymorphism        ( + )           ( __add__ )
# 2. inheritance   ( class lb(kg): )     ( __init__ )
# 3. encapsulation    ( __weight )       ( a.weight = 10 )

class Weight:
    def __init__(self, w):
        self.weight = w

class kg(Weight):
    def __str__(self):
        return str(self.weight) + " kg"

    def __add__(self, other):
        if "kg" in other.__str__():
            return kg(self.weight + other.weight)
        elif "lb" in other.__str__():
            return kg(self.weight + (other.weight / 2.2))

class lb(Weight):
    def __str__(self):
        return str(self.weight) + " lb"

    def __add__(self, other):
        if "lb" in other.__str__():
            return lb(self.weight + other.weight)
        elif "kg" in other.__str__():
            return lb(self.weight + (other.weight * 2.2))

x = kg(1)
y = lb(2.2)

print(f"{x} + {y} = {x + y}")
print(f"{y} + {x} = {y + x}")

a = x + y # 2.0 kg
b = y + x # 4.4 lb
print(a + b) # 4.0 kg
print(b + a) # 8.8 lb

# a.weight = 10
# print(a)

#################################################

# Data Hiding and Object Printing
1.  __var
2.  _str_
3.  _repr_
4.  print    -->  str  -->  repr  -->  default repr value ( memory address of obj )

#################################################

# weight.py
class kg:
    def __init__(self, w):
        self.weight = w

    def __str__(self):
        return str(self.weight) + " kg"

    def __repr__(self):
        return str(self.weight) + " kg"

    def __add__(self, other):
        if "kg" in other.__str__():
            return kg(self.weight + other.weight)
        elif "lb" in other.__str__():
            return kg(self.weight + (other.weight / 2.2))

    def __ge__(self, other):
        print("haha")

class lb(kg):
    def __str__(self):
        return str(self.weight) + " lb"

    def __repr__(self):
        return str(self.weight) + " lb"

    def __add__(self, other):
        if "lb" in other.__str__():
            return lb(self.weight + other.weight)
        elif "kg" in other.__str__():
            return lb(self.weight + (other.weight * 2.2))

#print(__name__)# "__main__", "file name"

if __name__ == "__main__":
    x = kg(1)
    y = lb(2.2)
    print(f"{x} + {y} = {x + y}")
    print(f"{y} + {x} = {y + x}")

#if __name__ == "oop_concept_pattern":
#    print("work when import")

#################################################

# not __repr__()

>> from weight import kg, lb
>> x = kg(1)
>> x
<weight.kg object at 0x7b677e51f0>
>> f"{x}"
'1 kg'
>> y = lb(2.2)
>> y
<weight.lb object at 0x7b67748880>
>> x + y
<weight.kg object at 0x7b677488b0>
>>

#################################################

# with __repr__()
>> from weight import kg,lb
>> x = kg(1)
>> x
1 kg
>> y = lb(2.2)
>> y
2.2 lb
>> x + y
2.0 kg
>> y + x
4.4 lb
>>

#################################################

4. Abstraction

Abstract classes are the classes which contains one or more abstract method;

and abstract methods are the methods which does not contain any implemetation,

but the child-class need to implement these methods otherwise error will
be reported.

In this way, we can force the child-class to implement certain methods in it.

#################################################

# abstraction example.1
from abc import ABCMeta, abstractmethod

class Car(metaclass=ABCMeta):
    def __init__(self, b="ABS system brake"):
        self.brake_system = b

    def brake(self):
        print(f"Brake with {self.brake_system}")

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass

class City_car(Car):
    def __init__(self):
        super().__init__()
        self.engine = "city engine"
        self.tire = "city tire"

    def start(self):
        print(f"{self.engine} start.")

    def stop(self):
        print(f"{self.engine} stop.")


x = City_car()
x.start()
x.stop()
x.brake()

# y = Car()

################################################

# abstraction example.2
# crd freecodecamp

from abc import ABC, abstractmethod

class Book(ABC):
    def __init__(self, title, quantity, author, price):
        self.title = title
        self.quantity = quantity
        self.author = author
        self.__price = price
        self.__discount = None

    def set_discount(self, discount):
        self.__discount = discount

    def get_price(self):
        if self.__discount:
            return self.__price * (1 - self.__discount)
        return self.__price

    @abstractmethod
    def __repr__(self):
        return f"Book: {self.title}\nQuantity: {self.quantity}\nAuthor: {self.author}\nPrice: {self.get_price()}\n"

class Novel(Book):
    def __init__(self, title, quantity, author, price, pages):
        super().__init__(title, quantity, author, price)
        self.pages = pages

    def __repr__(self):
        return super().__repr__() + f"Pages: {self.pages}\n"

class Academic(Book):
    def __init__(self, title, quantity, author, price, branch):
        super().__init__(title, quantity, author, price)
        self.branch = branch

    def __repr__(self):
        return super().__repr__() + f"Branch: {self.branch}\n"


novel1 = Novel('Two States', 20, 'Chetan Bhagat', 300, 200)
novel1.set_discount(0.20)

academic1 = Academic('Python Foundations', 12, 'PSF', 300, 'IT')

print(novel1)
print(academic1)

# del @abstractmethod
#b = Book("book1", 10, "abc", 10)
#print(b)

################################################

Method Overloading:

Two or more methods have the same name but different numbers of parameters or
different types of parameters, or both.

These methods are called overloaded methods and this is called method overloading.

Like other languages (for example, method overloading in C++) do,
python does not support method overloading by default.

But there are different ways to achieve method overloading in Python.

#################################################

# Python doesn't support Method Overloading by default.

class X:
    def __init__(self, value):
        self.value = value

    def add(self, other):
        print(self.value + other)

    def add(self, other1, other2):# li
        print(self.value + other1 + other2)


a = X(1)
a.add(1, 2) # lifo

###########

001 --> fun obj
add --> 001

002 --> fun obj
add --> 002

###########

from multipledispatch import dispatch

# method overloading
class X:
    def __init__(self, value):
        self.value = value

    @dispatch(int)
    def add(self, other):
        print(self.value + other)

    @dispatch(int, int)
    def add(self, other1, other2): # li
        print(self.value + other1 + other2)

a = X(1)
a.add(1) # lifo

###########

# python style
class X:
    def __init__(self, value):
        self.value = value

    def add(self, other1, other2=None):
        if not other2:
            print(self.value + other1)
        else:
            print(self.value + other1 + other2)

a = X(1)
a.add(1, 3) # lifo

###########

# python style
class X:
    def __init__(self, value):
        self.value = value

    def add(self, *other):
        t = self.value
        for n in other:
            t += n
        print(t)

a = X(1)
a.add(1, 2, 3, 1, 1, 1, 1, 1, 1)

#################################################

# Method Overloading by using dispatch decorator
# dispatch = ‌သီးသန့်‌ေနရာ
from multipledispatch import dispatch

@dispatch(int, int)
def product(first, second):
    result = first * second
    print(result, "   <--- int 2")

@dispatch(int, int, int)
def product(first, second, third):
    result = first * second * third
    print(result, "   <---  int 3 ")

@dispatch(float, float, float)
def product(first, second, third):
    result = first * second * third
    print(round(result), "   <---  float 3")

def product(*x):
    t = 0
    for i in x:
        t += i
    print(t)

product(1, 2)
product(1, 2, 3)
product(1.1, 2.1, 3.0)
#product(1, 2, 3, 4, 5, 0.1)

#################################################

2. Method overriding ( LIFO )
# override လွှမ်းမိုး

---> sub class method "overrides" the method provided in the base class.

class B:
    def f(self):
        print("b")

class S(B):
    def f(self):
        print("s")

s = S()
s.f()

################################################

Design Patterns & Python

What is a Design Pattern?
Design Patterns are concrete solutions for reoccurring problems.
They satisfy the design principles and can be used to understand and illustrate them.
They provide a NAME to communicate effectively with other programmers.

#################################################

1. Iterator Pattern
The essence of the Iterator Factory method Pattern is to
"Provide a way to access the elements of an aggregate object sequentially
without exposing its underlying representation."
.

aggregate ( စုပေါင်း )
exposing ( မြင်သာအောင်ပြ )
representation ( ကိုယ်စားပြု )

#################################################

2. Decorator Pattern
( မူလအရာကို မထိခိုက်ဘဲ  မွမ်းမံနိုင်စွမ်း )
The decorator pattern is a design pattern that
allows behavior to be added to an existing object dynamically.
behaviour ( အပြုအမူ လုပ်ဆောင်ချက် )

#################################################

3. Strategy Pattern
The strategy pattern (also known as the policy pattern) is
a particular software design pattern,
whereby algorithms behavior can be selected at runtime.

#################################################

4. Adapter Pattern
The adapter pattern is a design pattern that
translates one interface for a class into a compatible interface

#################################################

# 1. Iterator Pattern
class MyIter():
    def __init__(self, v):
        self.v = v #(1, 2, 3, "apple", "banana")
        self.p = 0

    def __next__(self):
        try:
            value = self.v[self.p]# 1
            self.p += 1
            # print ("Iteration done.")
            return value
        except IndexError:
            raise StopIteration()

    def __iter__(self):
        print("------->   work iter of myiter")
        return self

###########

class Reverse_iter():
    def __init__(self, v):
        self.v = v #(1, 2, 3, "apple", "banana")
        self.p = 1 # minus pos

    def __next__(self):
        try:
            value = self.v[-self.p]# 1
            self.p += 1
            # print ("Iteration done.")
            return value
        except IndexError:
            raise StopIteration()

    def __iter__(self):
        print("------->   work iter of reverse iter")
        return self

###########

class My_obj():
    def __init__(self, *items):
        self.items = items # (1, 2, 3, "apple", "banana")

    def __iter__(self):
        print("------->   work iter of my obj")
        return MyIter(self.items)

###########

class A:
    def __init__(self, *items):
        self.items = items

    def __iter__(self):
        print("------->   work iter of A")
        return Reverse_iter(self.items)

###########

obj = My_obj(1, 2, 3, "apple", "banana")
for item in obj:
    print(item)

print("- " * 30 )

obj1 = A(1, 2, 3, "apple", "banana")
for item in obj1:
    print(item)

print("- " * 30 )

###########

obj2 = MyIter([1, 2, 3, "apple", "banana"])
for i in obj2:
    print(i)

print("- " * 30 )

obj2 = Reverse_iter([1, 2, 3, "apple", "banana"])
for i in obj2:
    print(i)

print("- " * 30 )

###########

for i in "abcdefg1436":
    print(i)

#################################################

# 2. Decorator Pattern
class UnderlineWrapper:
    def __init__(self, obj):
        self.obj = obj

    def render(self):
        return "<u>{}</u>".format(self.obj.render())

class ItalicWrapper:
    def __init__(self, obj):
        self.obj = obj

    def render(self):
        return "<i>{}</i>".format(self.obj.render())

class BoldWrapper:
    def __init__(self, obj):
        self.obj = obj

    def render(self):
        return "<b>{}</b>".format(self.obj.render())

class HeaderWrapper:
    def __init__(self, obj):
        self.obj = obj

    def render(self):
        return "<h1>{}</h1>".format(self.obj.render())

class UnderlineWrapper:
    def __init__(self, obj):
        self.obj = obj

    def render(self):
        return "<u>{}</u>".format(self.obj.render())

class WrittenText:
    def __init__(self, obj):
        self.obj = obj

    def render(self):
        return self.obj

x = WrittenText("Myself")
z = BoldWrapper(x)
print(x.render())
print(z.render())

y = UnderlineWrapper(z)
print(y.render())

###

x = WrittenText("Myself")

ih = ItalicWrapper(UnderlineWrapper(BoldWrapper(HeaderWrapper(x))))
print(ih.render())

nh = UnderlineWrapper(BoldWrapper(HeaderWrapper(x)))
print(nh.render())

print(x.render())

#################################################

# 3. strategy pattern
# runtime မှာ ရွေးချယ် လုပ်နိုင်စွမ်း

class IR_system:
    def __init__(self):
        self.sensor = "Electro optical targeting system(IR)"

    def search_target(self):
        print(f"{self.sensor} search infrared radiation of the target.")

class Radar_system:
    def __init__(self):
        self.sensor = "APG-81"

    def search_target(self):
        print(f"{self.sensor} search high frequency electro-magnetic waves that are reflected of the target.")

# strategy pattern
class Projectile:
    def __init__(self, system):
        self.system = system

    def search_target(self):
        self.system.search_target()

missile = Projectile(Radar_system())
missile.search_target()

missile1 = Projectile(IR_system())
missile1.search_target()

#######

class IR_missile(Projectile):
    def __init__(self):
        self.system = IR_system()

class Radar_missile(Projectile):
    def __init__(self):
        self.system = Radar_system()

#################################################

# 4. adaptor pattern

class IR_system:
    def __init__(self):
        self.sensor = "Electro optical targeting system"

    def search_target(self):
        print(f"{self.sensor} search infrared radiation of the target.")

class Radar_system:
    def __init__(self):
        self.sensor = "APG-81"

    def search_target(self):
        print(f"{self.sensor} search high frequency electro-magnetic waves that are reflected of the target.")

class Gps_system:
    def __init__(self):
        self.sensor = "GPS system"

    def search_target(self):
        print(f"{self.sensor} will guide missile.")

# adapter pattern
class Gps_adapter:
    def __init__(self, missile):
        self.missile = missile
        self.system = Gps_system()

    def search_target(self):
        self.system.search_target()# gps
        self.missile.search_target()

class IR_adapter:
    def __init__(self, missile):
        self.missile = missile
        self.system = IR_system()

    def search_target(self):
        self.system.search_target()  # ir
        self.missile.search_target()

class Radar_adapter:
    def __init__(self, missile):
        self.missile = missile
        self.system = Radar_system()

    def search_target(self):
        self.system.search_target()#radar
        self.missile.search_target()

class Projectile:
    def __init__(self, system):
        self.system = system

    def search_target(self):
        self.system.search_target()

# decorator / lifo
g_r_i = Gps_adapter(Radar_adapter(Projectile(IR_system())))
g_r_i.search_target()
print(" -" * 40)

# decorator
g_r_i = Radar_adapter(Gps_adapter(Projectile(IR_system())))
g_r_i.search_target()

"""

