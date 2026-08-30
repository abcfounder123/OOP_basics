
"""

Design Pattern (23)

Creational Patterns (5)
1. Factory Method
2. Abstract Factory
3. Builder
4. Prototype
5. Singleton

Structural Patterns (7)
1. Adapter
2. Bridge
3. Composite
4. Decorator
5. Facade
6. Flyweight
7. Proxy

Behavioral Patterns (11)
1. Chain of Responsibility
2. Command
3. Interpreter
4. Iterator
5. Mediator
6. Memento
7. Observer
8. State
9. Strategy
10. Template Method
11. Visitor

-------------------------------------------------

Creational Patterns (5)
1. Factory Method
2. Abstract Factory
3. Builder
4. Prototype
5. Singleton

-------------------------------------------------

1. Factory Method


class King:
    def work(self):
        print("King is working.")


class Soldier:
    def work(self):
        print("Soldier is working.")


def factory(role):
    if role == "King":
        return King()
    elif role == "Soldier":
        return Soldier()


p1 = factory("King")
p1.work()

p2 = factory("Soldier")
p2.work()

-------------------------------------------------

2. Abstract Factory


class King:
    def work(self):
        print("King is working.")


class Soldier:
    c = 0
    def __init__(self):
        Soldier.c += 1
        self.n = Soldier.c

    def work(self):
        print("Soldier is working.")

    def __repr__(self):
        return f"Soldier No.{self.n}"


class Kingdom:
    def create_king(self):
        return King()

    def create_soldier(self):
        return Soldier()


def setup_team(factory):
    king = factory.create_king()
    soldiers = [factory.create_soldier() for i in range(10000)]

    king.work()
    soldiers[0].work()
    print(soldiers)


setup_team(Kingdom())

-------------------------------------------------

3. Builder

b1.teach_html_css().teach_python().teach_design_pattern().teach_sql().build()

-------------------------------------------------

4. Prototype

def clone(self):
    return deepcopy(self)
    
-------------------------------------------------

"Example of Builder and Prototype"
 

from copy import deepcopy


class Employee:
    def __init__(self):
        self.skill = []

    def add_skill(self, skill):
        self.skill.append(skill)

    def clone(self):
        return deepcopy(self)


class EmployeeBuilder:
    def __init__(self):
        self.employee = Employee()

    def teach_python(self):
        self.employee.add_skill("Python")
        return self

    def teach_design_pattern(self):
        self.employee.add_skill("Design patterns(23)")
        return self

    def teach_sql(self):
        self.employee.add_skill("SQL")
        return self

    def teach_html_css(self):
        self.employee.add_skill("HTML")
        self.employee.add_skill("CSS")
        return self

    def build(self):
        return self.employee


b1 = EmployeeBuilder()

leader = b1.teach_html_css().teach_python().teach_design_pattern().teach_sql().build()
print(leader)

new_leader = leader.clone()
print(new_leader)

-------------------------------------------------

5. Singleton


class King:
    king = None

    def __new__(cls):
        if cls.king is None:
            cls.king = super().__new__(cls)
        return cls.king

    def work(self):
        print("King is working.")


k = King()
print(k)

k2 = King()
print(k2)

--------------------------------------------------------------------------------------------------

Structural Patterns (7)
1. Adapter
2. Bridge
3. Composite
4. Decorator
5. Facade    (complex to easy)
6. Flyweight (reduce weight, share)
7. Proxy

-------------------------------------------------

1. Adapter

# Target
class Engine:
    def on(self):
        print("Diesel Engine On.")


class NewEngine:
    def start(self):
        print("Pertol Engine On.")


class Adapter:
    def __init__(self, new_engine):
        self.new_engine = new_engine

    def on(self):
        self.new_engine.start()


e1 = Engine()
e2 = Adapter(NewEngine())

e1.on()
e2.on()

-------------------------------------------------

2. Bridge
   - Implementation  (worker)
   - Abstraction     (controller)


class TV:
    def on(self):
        print("TV ON.")


class AC:
    def on(self):
        print("AC ON.")


class Fan:
    def on(self):
        print("Fan ON.")


class RemoteControl:
    def __init__(self, device):
        self.device = device

    def power(self):
        self.device.on()


class SmartRemoteControl:
    def __init__(self, device):
        self.device = device

    def power(self):
        self.device.on()
        print("Opened your device.")


r1 = RemoteControl(TV())
r1.power()

r2 = SmartRemoteControl(Fan())
r2.power()

-------------------------------------------------

3. Composite
   - Leaf + Composite + Component(interface)
   - eg. File System  =>  File, Folder


from abc import ABC, abstractmethod


class EmployeeSystemCompontent(ABC):
    @abstractmethod
    def show_detail(self):
        pass


# Leaf
class Employee(EmployeeSystemCompontent):
    def __init__(self, name):
        self.name = name

    def show_detail(self):
        print(f"  - Employee ({self.name})")


# Composite
class Department(EmployeeSystemCompontent):
    def __init__(self, name):
        self.name = name
        self.members = []

    def add(self, member):
        self.members.append(member)

    def show_detail(self):
        print(f"Department ({self.name})")
        for m in self.members:
            m.show_detail()


p1 = Employee("Mg Mg")
p2 = Employee("Ma Ma")
p3 = Employee("Hla Hla")

p4 = Employee("U Ba")
p5 = Employee("Daw Mya")

i = Department("IT Department")
i.add(p1)
i.add(p2)
i.add(p3)

h = Department("HR Department")
h.add(p4)
h.add(p5)

company = Department("Main Department")
company.add(i)
company.add(h)

p1.show_detail()
print()

h.show_detail()
print()

i.show_detail()
print()

company.show_detail()
print()
                
-------------------------------------------------

4. Decorator


class Employee():
    def __init__(self, name):
        self.name = name

    def show_detail(self):
        print(f"  - Employee ({self.name})")

    def role(self):
        return "Normal Employee"


class TeamLeadDecorator:
    def __init__(self, employee):
        self.employee = employee

    def role(self):
        return f"{self.employee.role()} + Team Leader"


p1 = Employee("Mg Mg")
p2 = Employee("Ma Ma")
p3 = Employee("Hla Hla")

p3 = TeamLeadDecorator(p3)

print(p1.role())
print(p2.role())
print(p3.role())

-------------------------------------------------

5. Facade    (complex to easy)


class LightSystem:
    def dim(self):
        print("Reduce Light")


class Projector:
    def on(self):
        print("Projector ON.")


class SoundSystem:
    def set_volume(self):
        print("Set volume to 75 %")


class DVDPlayer:
    def play(self):
        print("Movies starts.")


class TheaterFacade:
    def __init__(self):
        self.light = LightSystem()
        self.projector = Projector()
        self.sound = SoundSystem()
        self.dvd = DVDPlayer()

    def watch_movies(self):
        self.light.dim()
        self.projector.on()
        self.sound.set_volume()
        self.dvd.play()
        
    def close(self):
        pass


t = TheaterFacade()
t.watch_movies()

-------------------------------------------------

6. Flyweight (reduce weight, share)


class Dollar:
    x = {}

    def __new__(cls, n):
        if n not in cls.x:
            self = super().__new__(cls)
            self.n = n
            cls.x[n] = self

        return cls.x[n]


x = Dollar(1)
y = Dollar(1)
print(x)
print(y)
print(Dollar.x)

<__main__.Dollar object at 0x104b36e10>
<__main__.Dollar object at 0x104b36e10>
{1: <__main__.Dollar object at 0x104b36e10>}

-------------------------------------------------

7. Proxy

class Account:
    def __init__(self, user_name):
        self.user_name = user_name
        self.password = None

    def set_password(self, password):
        self.password = password


class PasswordProxy:
    def __init__(self, account):
        self.account = account

    def set_password(self, password):
        if len(password) >= 8:
            self.account.set_password(password)
        else:
            print("Password must be more than 8 characters.")


account = Account("Mg Mg")
proxy = PasswordProxy(account)

proxy.set_password("1234567")

-------------------------------------------------

"""


