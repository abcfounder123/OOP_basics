
"""
Attributes exercises

Step.1   --->   Write

1. Laptop တွင် serial_no ပါသည်။ on, off လုပ်နိုင်သည်။

2. Network_Card တွင် speed ပါသည်။ သတ်မှတ် speed ဖြင့် download ဆွဲနိုင်သည်။

3. 1995 တွင် ပေါ်ပေါက်ခဲ့သော DialUp ဟူသော network card အမျိုးအစား၏ download ဆွဲနိုင်သော အမြန်နှုန်း speed သည် 9600bit/s ဖြစ်သည်။
ထိုအမြန်နှုန်းဖြင့် download ဆွဲနိုင်သည်။

4. 1999 တွင် ပေါ်ပေါက်ခဲ့သော ADSL ဟူသော network card အမျိုးအစား၏ download ဆွဲနိုင်သော အမြန်နှုန်း speed သည် 2000000bit/s (2Mbit/s)  ဖြစ်သည်။
ထိုအမြန်နှုန်းဖြင့် download ဆွဲနိုင်သည်။

5. 2006 တွင် ပေါ်ပေါက်ခဲ့သော Ethernet ဟူသော network card အမျိုးအစား၏ download ဆွဲနိုင်သော အမြန်နှုန်း speed သည် 10Mbit/s  ဖြစ်သည်။
ထိုအမြန်နှုန်းဖြင့် download ဆွဲနိုင်သည်။

6. 2014 တွင်  Ethernet_2014 ဟူသော network card အမျိုးအစား၏ download ဆွဲနိုင်သော အမြန်နှုန်း speed သည် 10000Mbit/s  ( တစ်စက္ကန့်လျှင် 1250 မီဂါဘိုက်) ဖြစ်သည်။
ထိုအမြန်နှုန်းဖြင့် download ဆွဲနိုင်သည်။

7. Car မှာ ကားနံပါတ် တာယာနဲ့ အင်ဂျင်ပါတယ်။ (VIN, tires, engine)

8. Tires ( ကားတာယာ ) တွင် size နှင့် pressure ပါသည်။
pressure ၏ မူလတန်ဖိုးသည် 0 ( psi ) ဖြစ်သည်။
လေထိုးသောလုပ်ဆောင်ချက်ပါသည်။ သတ်မှတ်ပေးလိုက်သော ဖိအားအတိုင်း လေထိုးပေးမည်။

9. Engine တွင် fuel_type ပါသည်။
စက်နှိုး/မနှိုး ဟူသော အခြေအနေ  state ပါသည်။
မူလအခြေအနေမှာ စက်မနှိုးထားသဖြင့် off ဖြစ်နေမည်။
ပေးထားသော fuel_type ဖြင့် စက်နှိုး ၊ စက်ရပ် မည့်လုပ်‌ဆောင်ချက်ပါသည်။ ( on(), off() )

###################################################################################################

Step.2   --->   Divide

class   --->   
data    --->   
method  ---> 

1. Laptop တွင် serial_no ပါသည်။ on, off လုပ်နိုင်သည်။
class   --->   Laptop
data attributes   --->   serial_no
method attributes --->   on(), off()

2. Network_Card တွင် speed ပါသည်။ သတ်မှတ် speed ဖြင့် download ဆွဲနိုင်သည်။
class   --->  Network_Card 
data    --->  speed 
method  --->  download() 

3. 1995 တွင် ပေါ်ပေါက်ခဲ့သော DialUp ဟူသော network card အမျိုးအစား၏ download ဆွဲနိုင်သော အမြန်နှုန်း speed သည် 9600bit/s ဖြစ်သည်။
ထိုအမြန်နှုန်းဖြင့် download ဆွဲနိုင်သည်။
class   ---> DialUp  
data    ---> speed = 9600bit/s 
method  ---> download() 

4. 1999 တွင် ပေါ်ပေါက်ခဲ့သော ADSL ဟူသော network card အမျိုးအစား၏ download ဆွဲနိုင်သော အမြန်နှုန်း speed သည် 2000000bit/s (2Mbit/s)  ဖြစ်သည်။
ထိုအမြန်နှုန်းဖြင့် download ဆွဲနိုင်သည်။

class   --->  ADSL 
data    --->  speed = 2000000bit/s (2Mbit/s) 
method  --->  download()

5. 2006 တွင် ပေါ်ပေါက်ခဲ့သော Ethernet ဟူသော network card အမျိုးအစား၏ download ဆွဲနိုင်သော အမြန်နှုန်း speed သည် 10Mbit/s  ဖြစ်သည်။
ထိုအမြန်နှုန်းဖြင့် download ဆွဲနိုင်သည်။
class   --->  Ethernet 
data    --->  speed = 10Mbit/s 
method  --->  download()

6. 2014 တွင်  Ethernet_2014 ဟူသော network card အမျိုးအစား၏ download ဆွဲနိုင်သော အမြန်နှုန်း speed သည် 10000Mbit/s  ( တစ်စက္ကန့်လျှင် 1250 မီဂါဘိုက်) ဖြစ်သည်။
ထိုအမြန်နှုန်းဖြင့် download ဆွဲနိုင်သည်။
class   --->  Ethernet_2014 
data    --->  speed = 10000Mbit/s  ( တစ်စက္ကန့်လျှင် 1250 မီဂါဘိုက်) 
method  --->  download()

7. Car မှာ ကားနံပါတ် တာယာနဲ့ အင်ဂျင်ပါတယ်။ (VIN, tires, engine)
class   --->  Car 
data    --->  VIN, tires, engine 
method  ---> 

8. Tires ( ကားတာယာ ) တွင် size နှင့် pressure ပါသည်။
pressure ၏ မူလတန်ဖိုးသည် 0 ( psi ) ဖြစ်သည်။
လေထိုးသောလုပ်ဆောင်ချက်ပါသည်။ သတ်မှတ်ပေးလိုက်သော ဖိအားအတိုင်း လေထိုးပေးမည်။
class   --->  Tires 
data    --->  size, pressure = 0
method  --->  pump(p)

def pump():
    print(f"pump to 0 psi.")


def pump(p):
    print(f"pump to {p} psi.")


9. Engine တွင် fuel_type ပါသည်။
စက်နှိုး/မနှိုး ဟူသော အခြေအနေ  state ပါသည်။
မူလအခြေအနေမှာ စက်မနှိုးထားသဖြင့် off ဖြစ်နေမည်။
ပေးထားသော fuel_type ဖြင့် စက်နှိုး ၊ စက်ရပ် မည့်လုပ်‌ဆောင်ချက်ပါသည်။ ( on(), off() )
class   --->  Engine  
data    --->  fuel_type, state = "off"
method  --->  on(), off()

###################################################################################################

Car မှာ ကားနံပါတ် တာယာနဲ့ အင်ဂျင်ပါတယ်။ (VIN, tires, engine)
Tires ( ကားတာယာ ) တွင် size နှင့် pressure ပါသည်။
pressure ၏ မူလတန်ဖိုးသည် 0 ( psi ) ဖြစ်သည်။
လေထိုးသောလုပ်ဆောင်ချက်ပါသည်။ သတ်မှတ်ပေးလိုက်သော ဖိအားအတိုင်း လေထိုးပေးမည်။
Engine တွင် fuel_type ပါသည်။
စက်နှိုး/မနှိုး ဟူသော အခြေအနေ  state ပါသည်။
မူလအခြေအနေမှာ စက်မနှိုးထားသဖြင့် off ဖြစ်နေမည်။
ပေးထားသော fuel_type ဖြင့် စက်နှိုး ၊ စက်ရပ် မည့်လုပ်‌ဆောင်ချက်ပါသည်။ ( on(), off() )

class   --->   Car
data    --->   VIN, tires, engine
method  --->

class   --->  Tires 
data    --->  size, pressure = 0 
method  --->  pump(p)

class   --->  Engine 
data    --->  fuel_type, state = off 
method  --->  on(), off()

#################################################

Prefix data or external data 


class Tires:
    def __init__(self):
        self.pressure = 0         <--- prefix data


class Laptop:
    def __init__(self, x):
        self.serial_no = x       <--- external data 


#################################################

Function with obj data


def download(self):
    print("Download with", self.speed)


#################################################

Function with obj data + external data


def pump(self, p):
    print(f"pump to {p} psi.")


#################################################

class Tire:
    def __init__(self, s):
        self.size = s
        self.pressure = 0

    def pump(self, p):
        print(f"Pump to {p} psi.")
        self.pressure = p


t1 = Tire(15)     # Mandalay

t2 = Tire(18)     # Yangon

print(t1.pressure)
t1.pump(7)
print(t1.pressure)

t2.pump(10)
print(t2.pressure)

print(id(t1))
print(id(t2))

x = Tire(15)     # Mandalay
y = x            # Mandalay

#################################################

1. House design           <---  paper                   class Tire
2. Python => Computer     <---  create                  Tire(15)
3. house1, house2         <---  Mandalay, Yangon        4298171472, 4298171520
4. Label1                 <---- Mandalay                4298171520

###################################################################################################

Car မှာ ကားနံပါတ် တာယာနဲ့ အင်ဂျင်ပါတယ်။                              Car     (VIN, tires, engine)
Tires ( ကားတာယာ ) တွင် size နှင့် pressure ပါသည်။  
pressure ၏ မူလတန်ဖိုးသည် 0 ( psi ) ဖြစ်သည်။                       Tires       (size, pressure = 0), pump(p) 
လေထိုးသောလုပ်ဆောင်ချက်ပါသည်။ သတ်မှတ်ပေးလိုက်သော ဖိအားအတိုင်း လေထိုးပေးမည်။
Engine တွင် fuel_type ပါသည်။
စက်နှိုး/မနှိုး ဟူသော အခြေအနေ  state ပါသည်။
မူလအခြေအနေမှာ စက်မနှိုးထားသဖြင့် off ဖြစ်နေမည်။
ပေးထားသော fuel_type ဖြင့် စက်နှိုး ၊ စက်ရပ် မည့်လုပ်‌ဆောင်ချက်ပါသည်။ Engine  (fuel_type, state = off) ( on(), off() )

#################################################

class   --->   Car
data    --->   VIN, tires, engine
method  --->

class   --->  Tires 
data    --->  size, pressure = 0 
method  --->  pump(p)

class   --->  Engine 
data    --->  fuel_type, state = off 
method  --->  on(), off()


class   --->  Car
data    --->  VIN, tires, engine
method  --->

#################################################


class Car:
    def __init__(self, VIN, tires, engine):
        self.VIN = VIN
        self.tires = tires
        self.engine = engine


class Tires:
    def __init__(self, size):
        self.size = size
        self.pressure = 0

    def pump(self, p):
        print(f"pump to {p} psi.")


class Engine:
    def __init__(self, fuel_type):
        self.fuel_type = fuel_type
        self.state = "off"

    def on(self):
        print(f"{self.fuel_type} Engine On.")

    def off(self):
        print(f"{self.fuel_type} Engine Off.")


# city_car -> "BMW-0001", 15" tires, Petrol engine
# 7psi, on

city_car = Car(VIN="BMW-0001", tires=Tires(15), engine=Engine("Petrol"))
city_car.tires.pump(7)
city_car.engine.on()

##################################################################################################

Step.4   --->   Controlling data by function  ( pressure, state )


class Car:
    def __init__(self, VIN, tires, engine):
        self.VIN = VIN
        self.tires = tires
        self.engine = engine


class Tires:
    def __init__(self, size):
        self.size = size
        self.pressure = 0

    def pump(self, p):
        print(f"pump to {p} psi.")
        self.pressure = p


class Engine:
    def __init__(self, fuel_type):
        self.fuel_type = fuel_type
        self.state = "off"

    def on(self):
        print(f"{self.fuel_type} Engine On.")
        self.state = "on"

    def off(self):
        print(f"{self.fuel_type} Engine Off.")
        self.state = "off"


# city_car -> "BMW-0001", 15" tires, Petrol engine
# 7psi, on

city_car = Car(VIN="BMW-0001", tires=Tires(15), engine=Engine("Petrol"))

print(city_car.engine.state)
city_car.engine.on()
print(city_car.engine.state)

#################################################

Step.5   --->   Controlling function by data  ( on(), off() )


class Car:
    def __init__(self, VIN, tires, engine):
        self.VIN = VIN
        self.tires = tires
        self.engine = engine


class Tires:
    def __init__(self, size):
        self.size = size
        self.pressure = 0

    def pump(self, p):
        print(f"pump to {p} psi.")
        self.pressure = p


class Engine:
    def __init__(self, fuel_type):
        self.fuel_type = fuel_type
        self.state = "off"

    def on(self):
        if self.state == "off":
            print(f"{self.fuel_type} Engine On.")
            self.state = "on"
        else:
            print("Already ON.")

    def off(self):
        if self.state == "on":
            print(f"{self.fuel_type} Engine Off.")
            self.state = "off"
        else:
            print("Already OFF.")
            
            
city_car = Car(VIN="BMW-0001", tires=Tires(15), engine=Engine("Petrol"))

city_car.engine.on()
city_car.engine.on()
city_car.engine.on()
city_car.engine.on()

city_car.engine.off()
city_car.engine.off()
city_car.engine.off()

##################################################################################################

1. Write
2. Divide
3. Draw
4. Controlling data
5. Controlling fun

#################################################

Step.6   --->  Auto create data (serial number) 

n = 0
Car.n += 1
self.VIN = f"BMW-{Car.n:0>4}"

#################################################


class Tires:
    def __init__(self, size):
        self.size = size
        self.pressure = 0

    def pump(self, p):
        print(f"pump to {p} psi.")
        self.pressure = p


class Engine:
    def __init__(self, fuel_type):
        self.fuel_type = fuel_type
        self.state = "off"

    def on(self):
        if self.state == "off":
            print(f"{self.fuel_type} Engine On.")
            self.state = "on"
        else:
            print("Already ON.")

    def off(self):
        if self.state == "on":
            print(f"{self.fuel_type} Engine Off.")
            self.state = "off"
        else:
            print("Already OFF.")


class Car:
    n = 0

    def __init__(self, *, tires, engine):
        Car.n += 1
        self.VIN = f"BMW-{Car.n:0>4}"
        self.tires = tires
        self.engine = engine

car1 = Car(tires=Tires(15), engine=Engine("Petrol"))
car2 = Car(tires=Tires(15), engine=Engine("Petrol"))

cars = []

for _ in range(1000):
    car = Car(tires=Tires(15), engine=Engine("Petrol"))
    cars.append(car)


for car in cars:
    print(car.VIN)


#################################################

Step.7   --->   Representation string  ( memory address to serial number )     


def __repr__(self):
    return f"<__main__.Car object at {hex(id(self))}>"


def __repr__(self):
    return self.VIN


<__main__.Car object at 0x1028bc2c0>    =>   "BMW-0001"            ->   self.VIN

<__main__.Tires object at 0x1010eb3e0>   =>   "15 inches tires"    ->   f"{self.size} inches tires"  

<__main__.Engine object at 0x102a9f470>  =>   "Petrol engine"      ->   f"{self.fuel_type} engine"  

#################################################


class Car:
    n = 0

    def __init__(self, *, tires, engine):
        Car.n += 1
        self.VIN = f"BMW-{Car.n:0>4}"
        self.tires = tires
        self.engine = engine

    def __repr__(self):
        return self.VIN


class Tires:
    def __init__(self, size):
        self.size = size
        self.pressure = 0

    def pump(self, p):
        self.pressure = p
        print(f"pump to {p} psi.")

    def __repr__(self):
        return f"{self.size} inches tires"


class Engine:
    def __init__(self, fuel_type):
        self.fuel_type = fuel_type
        self.state = "off"

    def on(self):
        if self.state == "off":
            self.state = "on"
            print(f"{self.fuel_type} Engine On.")
        else:
            print("Already On")

    def off(self):
        if self.state == "on":
            self.state = "off"
            print(f"{self.fuel_type} Engine Off.")
        else:
            print("Already Off")

    def __repr__(self):
        return f"{self.fuel_type} engine" 


car1 = Car(tires=Tires(15), engine=Engine("Petrol"))
car2 = Car(tires=Tires(18), engine=Engine("Diesel"))

print(car1)
print(car2)

city_car1 = Car(tires=Tires(15), engine=Engine("Petrol"))
city_car2 = Car(tires=Tires(15), engine=Engine("Petrol"))


cars = [city_car1, city_car2]
print(cars[0])
print(cars)

print(car1.tires)
print(car2.tires)

print(car1.engine)
print(car2.engine)

##################################################################################################

Step.8   --->   Creating many objects

cars = []

for _ in range(1000):
    cars.append(Car(tires=Tires(15), engine=Engine("Petrol")))


##################################################################################################

Step.9   --->   Controlling many objects


1. All

for car in cars:
    car.tires.pump(7)
    car.engine.on()

#################################################

2. Odd serial number 

# car1, car3
# 0, 2, 4, 6, 8, ...
for car in cars[::2]:
    car.tires.pump(7)
    car.engine.on()

#################################################

3. Even serial number

# car.2, car.4
# 1, 3, 5 ...
for car in cars[1::2]:
    car.tires.pump(7)
    car.engine.on()

#################################################

4. Reverse  => [::-1]

# 1000, 999, ...
for car in cars[::-1]:
    car.tires.pump(7)
    car.engine.on()
    print(car)

#################################################

5. First 10  => [:10]

# 0 1 2 3 4 5 6 7 8 9   =>  stop = 10
for car in cars[:10]:
    car.tires.pump(7)
    car.engine.on()
    print(car)
    print("-" * 42)

#################################################

6. Last 10  => [-10:]

# -10, -9, -8, -7, -6, -5, -4, -3, -2, -1  => start = -10
for car in cars[-10:]:
    car.tires.pump(7)
    car.engine.on()
    print(car)
    print("-" * 42)

#################################################

7. Last 10 reverse  
   - Last 10 + reverse   => [-10:][::-1]

# -1, -2, ... -10                          => start=-1, stop=-11, step=-1
for car in cars[-1:-11:-1]:
    car.tires.pump(7)
    car.engine.on()
    print(car)
    print("-" * 42)

#################################################    


class Car:
    n = 0

    def __init__(self, *, tires, engine):
        Car.n += 1
        self.VIN = f"BMW-{Car.n:0>4}"
        self.tires = tires
        self.engine = engine

    def __repr__(self):
        return self.VIN + f"({self.tires}, {self.engine})"


class Tires:
    def __init__(self, size):
        self.size = size
        self.pressure = 0

    def pump(self, p):
        self.pressure = p
        print(f"pump to {p} psi.")

    def __repr__(self):
        return f"{self.size} inches tires({self.pressure} psi)"


class Engine:
    def __init__(self, fuel_type):
        self.fuel_type = fuel_type
        self.state = "off"

    def on(self):
        if self.state == "off":
            self.state = "on"
            print(f"{self.fuel_type} Engine On.")
        else:
            print("Already On")

    def off(self):
        if self.state == "on":
            self.state = "off"
            print(f"{self.fuel_type} Engine Off.")
        else:
            print("Already Off")

    def __repr__(self):
        return f"{self.fuel_type} engine({self.state})"


cars = []

for _ in range(100):
    cars.append(Car(tires=Tires(15), engine=Engine("Petrol")))

for car in cars:
    car.tires.pump(7)
    car.engine.on()
    print(car)
    print("-" * 42)

print(cars)

################################################################################################## 

step.10   --->  Reverse engineering  

1. Steps  => 1 to 9

2. Class name - 3

3. Attributes
Car    - VIN = auto, tires, engine
Tires  - size, pressure=0, pump(p)
Engine - fuel_type, state="0ff", on(), off()

4. Data (control)
   - pressure by pump()
   - state by on(), off()

5. Methods (control)
   - on() by state
   - off() by state

6. Magic methods, double underscore methods, dunder methods(name, symbols) 
   __init__    ->  construct
   __repr__    ->  representation string  ( "BMW-0001" ) 

7. 

cars = []
empty car list

for _ in range(1000):
repeat (1000 times)

for car in cars:
iterate

##################################################################################################

1. Write
2. Divide                           20 seconds
3. Draw                             90 seconds
4. Controlling data                 20 seconds
5. Controlling fun                  30 seconds
6. Auto create serial number        30 seconds
7. Representation string            10 seconds 
8. Creating many objects            30 seconds
9. Controlling many objects         30 seconds
10. Reverse engineering

4 min 20 seconds

3 min


##################################################################################################

"""
