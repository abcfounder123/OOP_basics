
"""
Iteration (for)

x = ["apple", "banana", "orange"]

for i in x:
    print(i)

print(x)

#################################################

1. Iterable objects(str, list, ... )
   - iter

2. Iterator
   - next

#################################################

obj + obj      =>   __add__
for i in obj:  =>   __iter__
Access order   =>   __next__

#################################################

representation string     =>   __repr__       return str obj
Iterable objects          =>   __iter__       return iterator obj
Iterator                  =>   __next__       return as you like

#################################################

1. Iterable objects


class X:
    def __iter__(self):
        return iterator_obj


#################################################

2. Iterator


class X:
    def __next__(self):
        return "abc"


#################################################

x = ["apple", "banana", "orange"]

for i in x:
    print(i)

print(x)

#################################################

Iteration process

for
>> x.iter()      => new obj("apple", "banana", "orange")

in        
>> next(new obj) => "apple"    => new obj("banana", "orange")
>> next(new obj) => "banana"   => new obj("orange")
>> next(new obj) => "orange"   => new obj()
>> next(new obj) =>  Error     => stop iteration

#################################################


class X:
    def __init__(self):
        self.data = ["apple", "banana", "orange"]
        self.n = 0

    def __next__(self):
        ans = self.n
        self.n += 1
        return self.data[ans]


a = X()
print(next(a))
print(next(a))
print(next(a))
        

#################################################

How to stop iteration?

=> raise StopIteration

#################################################

1. "Stop by IndexError"


class X:
    def __init__(self, data):
        self.data = data
        self.n = 0

    def __next__(self):
        ans = self.n
        self.n += 1

        try:
            return self.data[ans]

        except IndexError:
            raise StopIteration


class Y:
    def __init__(self, data):
        self.y = data
        self.n = -1

    def __next__(self):
        ans = self.n
        self.n += -1
        
        try:
            return self.y[ans]
        
        except IndexError:
            raise StopIteration

#################################################

2. "Stop by condition"

if total is 10, maximun positive index is 9.


class X:
    def __init__(self, data):
        self.data = data
        self.n = 0
        self.max_index = len(self.data) - 1

    def __next__(self):
        ans = self.n
        self.n += 1
        if ans > self.max_index:
            raise StopIteration
        return self.data[ans]


if total is 10, maximun negative index is -10.


class Y:
    def __init__(self, data):
        self.data = data
        self.n = -1
        self.max_index = - len(self.data)

    def __next__(self):
        ans = self.n
        self.n += -1
        if ans < self.max_index:
            raise StopIteration
        return self.data[ans]

#################################################

Changing iteration Style of list


                       list      

                        |

                     My_list     new  iter

#################################################


class Y:
    def __init__(self, data):
        self.y = data
        self.n = -1

    def __next__(self):
        ans = self.n
        self.n += -1
        
        try:
            return self.y[ans]
        
        except IndexError:
            raise StopIteration


class My_list(list):
    def __iter__(self):
        return Y(self)


x = list(["apple", "banana", "orange"])

for i in x:
    print(i)

print("-" * 42)

x = My_list(["apple", "banana", "orange"])

for i in x:
    print(i)  

#################################################

1/4


class Quarter:
    def __init__(self, data):
        self.data = data
        self.start = 0
        self.m = len(data) // 4
        self.end = self.m
        self.n = 0
        self.f = 2


    def __next__(self):
        self.n += 1

        start = self.start
        end = self.end

        self.start = self.end
        self.end = self.m * self.f

        self.f += 1

        if self.n == 5:
            raise StopIteration

        return self.data[start: end]
        
        
#################################################

Creating Iterable objects   =>  __iter__()


class Z:
    def __init__(self):
        self.data1 = ["apple", "banana", "orange", "mangoes",  "orange", "mangoes", "apple", "banana",]
        self.data2 = "123456"
        self.data3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

    def __iter__(self):
        return Y(self.data3)


x = Z()

for i in x:
    print(i)

##################################################################################################   

"""
