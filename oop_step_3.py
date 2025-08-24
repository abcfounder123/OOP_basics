"""

Step.3   --->   Draw

Draw

- name
  - UpperCamealCase

- data
  - external
  - fixed

- method
  - external ( pump(p) )
  - fixed

- init
  - initialization (first stage of somthing)
  - constructor

#################################################

1. 1. Laptop တွင် serial_no ပါသည်။ on, off လုပ်နိုင်သည်။

class   --->   Laptop
data    --->   serial_no
method  --->   on(), off()

class Laptop:
    def __init__(obj, serial_no):
        obj.serial_no = serial_no

    def on(obj):
        pass
        
    def off(obj):
        pass

#################################################

2. Network_Card တွင် speed ပါသည်။ သတ်မှတ် speed ဖြင့် download ဆွဲနိုင်သည်။

class   --->   NetworkCard
data    --->   speed
method  --->   download

class NetworkCard:
    def __init__(obj, speed):
        self.speed = speed

    def download(obj):
        pass

#################################################

3. 1995 တွင် ပေါ်ပေါက်ခဲ့သော DialUp ဟူသော network card အမျိုးအစား၏ download ဆွဲနိုင်သော အမြန်နှုန်း speed သည် 9600bit/s ဖြစ်သည်။
ထိုအမြန်နှုန်းဖြင့် download ဆွဲနိုင်သည်။

class   --->   DialUp
data    --->   speed = 9600bit/s
method  --->   download()

class DialUp:
    def __init__(obj):
        obj.speed = "9600bit/s"

    def download(obj):
        pass

#################################################

4. 1999 တွင် ပေါ်ပေါက်ခဲ့သော ADSL ဟူသော network card အမျိုးအစား၏ download ဆွဲနိုင်သော အမြန်နှုန်း speed သည် 2000000bit/s (2Mbit/s)  ဖြစ်သည်။
ထိုအမြန်နှုန်းဖြင့် download ဆွဲနိုင်သည်။

class   --->   ADSL
data    --->   speed = 2000000bit/s (2Mbit/s)
method  --->   download()


class ADSL:
    def __init__(obj):
        obj.speed = "2000000bit/s (2Mbit/s)"

    def download(obj):
        pass

#################################################

5. 2006 တွင် ပေါ်ပေါက်ခဲ့သော Ethernet ဟူသော network card အမျိုးအစား၏ download ဆွဲနိုင်သော အမြန်နှုန်း speed သည် 10Mbit/s  ဖြစ်သည်။
ထိုအမြန်နှုန်းဖြင့် download ဆွဲနိုင်သည်။

class   --->   Ethernet2006
data    --->   speed = 10Mbit/s
method  --->   download()

class Ethernet2006:
    def __init__(obj):
        obj.speed = "10Mbit/s"

    def download(obj):
        pass

#################################################

6. 2014 တွင်  Ethernet_2014 ဟူသော network card အမျိုးအစား၏ download ဆွဲနိုင်သော အမြန်နှုန်း speed သည် 10000Mbit/s  ( တစ်စက္ကန့်လျှင် 1250 မီဂါဘိုက်) ဖြစ်သည်။
ထိုအမြန်နှုန်းဖြင့် download ဆွဲနိုင်သည်။

class   --->   Ethernet2014
data    --->   speed = 10000Mbit/s (1250 MB/s)
method  --->   download()

class Ethernet2014:
    def __init__(obj):
        obj.speed = "10000Mbit/s (1250 MB/s)"

    def download(obj):
        print(f"download with {obj.speed} speed.")

#################################################

7. Car မှာ ကားနံပါတ် တာယာနဲ့ အင်ဂျင်ပါတယ်။ (VIN, tires, engine)

class   --->   Car
data    --->   VIN, tires, engine
method  --->

class Car:
    def __init__(obj, VIN, tires, engine):
        obj.VIN = VIN
        obj.tires = tires
        obj.engine = engine

#################################################

8. Tires ( ကားတာယာ ) တွင် size နှင့် pressure ပါသည်။
pressure ၏ မူလတန်ဖိုးသည် 0 ( psi ) ဖြစ်သည်။
လေထိုးသောလုပ်ဆောင်ချက်ပါသည်။ သတ်မှတ်ပေးလိုက်သော ဖိအားအတိုင်း လေထိုးပေးမည်။

class   --->   Tires
data    --->   size, pressure = 0 ( psi )
method  --->   pump(p)


class Tires:
    def __init__(obj, size):
        obj.size = size
        obj.pressure = 0

    def pump(obj, p):
        print(f"pump to {p} psi.")

#################################################

9. Engine တွင် fuel_type ပါသည်။
စက်နှိုး/မနှိုး ဟူသော အခြေအနေ  state ပါသည်။
မူလအခြေအနေမှာ စက်မနှိုးထားသဖြင့် off ဖြစ်နေမည်။
ပေးထားသော fuel_type ဖြင့် စက်နှိုး ၊ စက်ရပ် မည့်လုပ်‌ဆောင်ချက်ပါသည်။ ( on(), off() )

class   --->   Engine
data    --->   fuel_type, state = "off"
method  --->   on(), off()

class Engine:
    def __init__(obj, fuel_type):
        obj.fuel_type = fuel_type
        obj.state = "off"

    def on(obj):
        pass

    def off(obj):
        pass

#################################################









"""