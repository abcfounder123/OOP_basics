"""

Step.1   --->   Write

Car မှာ ကားနံပါတ် တာယာနဲ့ အင်ဂျင်ပါတယ်။ (VIN, engine, tires)

Tires ( ကားတာယာ ) တွင် size နှင့် pressure ပါသည်။
pressure ၏ မူလတန်ဖိုးသည် 0 ( psi ) ဖြစ်သည်။
လေထိုးသောလုပ်ဆောင်ချက်ပါသည်။ သတ်မှတ်ပေးလိုက်သော ဖိအားအတိုင်း လေထိုးပေးမည်။

Engine တွင် fuel_type ပါသည်။
စက်နှိုး/မနှိုး ဟူသော အခြေအနေ  state ပါသည်။
မူလအခြေအနေမှာ စက်မနှိုးထားသဖြင့် off ဖြစ်နေမည်။
ပေးထားသော fuel_type ဖြင့် စက်နှိုး ၊ စက်ရပ် မည့်လုပ်‌ဆောင်ချက်ပါသည်။ ( on(), off() )

ဖန်တီးခဲ့သော တာယာနှင့် အင်ဂျင်ကို ယူသုံးပြီး city_car တစ်စီးဖန်တီးပါ။
ကားနံပါတ်မှာ 001A ၊ တာယာမှာ 15 လက်မ၊ ဆီအမျိုးအစားမှာ petrol ဓါတ်ဆီ ဖြစ်သည်။

ထိုကားကို လေဖိအား 3 psi ထိလေထိုးပြီး စက်နှိုးပါ။

#################################################

Step.2   --->   Divide

class   --->   Car
data    --->   VIN, tires, engine
method  --->

class   --->   Tires
data    --->   size, pressure = 0 ( psi )
method  --->   pump(p)

class   --->   Engine
data    --->   fuel_type, state = "off"
method  --->   on(), off()

#################################################

Step.3   --->   Draw


class Car:
    def __init__(obj, VIN, tires, engine):
        obj.VIN = VIN
        obj.tires = tires
        obj.engine = engine


class Tires:
    def __init__(obj, size):
        obj.size = size
        obj.pressure = 0

    def pump(obj, p):
        print(f"pump to {p} psi.")


class Engine:
    def __init__(obj, fuel_type):
        obj.fuel_type = fuel_type
        obj.state = "off"

    def on(obj):
        print(f"{obj.fuel_type} engine On.")

    def off(obj):
        pass


#################################################

Step.4   --->   control pressure, state

->  obj.pressure = p

################################################

Step.5   --->   limit ON and OFF

if off: on
if on: off

################################################

Step.6   --->   auto create serial number

n = 0
Car.n += 1
self.VIN = f"BMW-{Car.n:0>4}A"

################################################

Step.7   --->   representation string

def __repr__(obj):
    return f"{obj.VIN}"

def __repr__(obj):
    return f"<__main__.Car object at {hex(id(obj))}>"


################################################

Step.8   --->   creating many obj

for _ in range(100):
    cars.append(Car(Tires(15), Engine("petrol")))

################################################

Step.9   --->   controlling many obj

# last 10 on
for car in cars[-10:]:
    car.engine.on()

################################################

Step.10   --->   reversed engineering


class Car:
    n = 0

    def __init__(obj, tires, engine):
        Car.n += 1
        obj.VIN = f"BMW-{Car.n:0>4}A"
        obj.tires = tires
        obj.engine = engine

    def __repr__(obj):
        return f"{obj.VIN} ({obj.engine.state})"


class Tires:
    def __init__(obj, size):
        obj.size = size
        obj.pressure = 0

    def pump(obj, p):
        obj.pressure = p
        print(f"pump to {p} psi.")


class Engine:
    def __init__(obj, fuel_type):
        obj.fuel_type = fuel_type
        obj.state = "off"

    def on(obj):
        if obj.state == "off":
            obj.state = "on"
            print(f"{obj.fuel_type} engine On.")
        else:
            print("Already ON.")

    def off(obj):
        if obj.state == "on":
            obj.state = "off"
            print(f"{obj.fuel_type} engine Off.")
        else:
            print("Already OFF.")


cars = []

for _ in range(100):
    cars.append(Car(Tires(15), Engine("petrol")))

for car in cars[1::2]:
    car.engine.on()

print(cars)

################################################################################################



"""