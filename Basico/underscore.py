"""
1. Use in Interpreter

Python automatically stores the value of the last expression in the interpreter to a particular variable called "_." You can also assign these value to another variable if you want.

You can use it as a normal variable.

Usar em terminal python
7 + 9
_
_ + 66
_
a = _
_ = _ + 543
_
a

"""
_ = 3 * 4
657 + 543

print(_)

"""
2. Ignoring Values

Underscore(_) is also used to ignore the values. If you don't want to use specific values while unpacking, just assign that value to underscore(_).

Ignoring means assigning the values to special variable underscore(_). We're assigning the values to underscore(_) given not using that in future code.
"""

## ignoring a value
a, _, b = (1, 2, 3) # a = 1, b = 3
print(a, b)


## ignoring multiple values
## *(variable) used to assign multiple value to a variable as list while unpacking
## it's called "Extended Unpacking", only available in Python 3.x
a, *_, b = (7, 6, 5, 4, 3, 2, 1)
print(a, b)

primeiro, *_, ultimo = (1, 2, 3, 4, 5, 6, 7, 8, 9)
print(ultimo, primeiro)
print(_)

first, *_ = {1:'carro', 2:'moto', 3:'onibus', 4:'caminhao', 5:'trator', 6:'ferramentas'}
print(_)
print(_[3]) # python trata o _ como uma lista


"""
3. Use in Looping

You can use underscore(_) as a variable in looping.
"""

## lopping ten times using _
for _ in range(5):
    print(_)

## iterating over a list using _
## you can use _ same as a variable
languages = ["Python", "JS", "PHP", "Java"]
for _ in languages:
    print(_)

_ = 5
while _ < 10:
    print(_, end = ' - ') # para deixar na mesma linha
    _ += 1

print()
_ = 5
while _ < 10:
    print(_, end = '\n') # default value of 'end' id '\n' in python. we're changing it to space
    _ += 1



"""
4. Separating Digits of Numbers

If you have a long digits number, you can separate the group of digits as you like for better understanding.

Ex:- million = 1_000_000

Next, you can also use underscore(_) to separate the binary, octal or hex parts of numbers.

Ex:- binary = 0b_0010, octa = 0o_64, hexa = 0x_23_ab
"""


## different number systems
## you can also check whether they are correct or not by coverting them into integer using "int" method
million = 1_000_000
binary = 0b_0010
octa = 0o_64
hexa = 0x_23_ab
hexa2 = 0x23ab

print("Milhão: ", million, type(million))
print("Binário: ", binary, type(binary))
print("Octagonal: ", octa, type(octa))
print("Hexagonal: ", hexa, type(hexa))

print("Hexa 2 (sem _): ", hexa2)

"""
5. Naming Using Underscore(_)

Underscore(_) can be used to name variables, functions and classes, etc..,

    Single Pre Underscore:- _variable

    Signle Post Underscore:- variable_

    Double Pre Underscores:- __variable

    Double Pre and Post Underscores:- __variable__

5.1. _single_pre_underscore

_name

Single Pre Underscore is used for internal use. Most of us don't use it because of that reason.
"""

class Test:

    def __init__(self):
        self.name = "datacamp"
        self._num = 7

obj = Test()
print(obj.name)
print(obj._num)


"""
5.3. Double Pre Underscore

__name

Double Pre Underscores are used for the name mangling.

Double Pre Underscores tells the Python interpreter to rewrite the attribute name of subclasses to avoid naming conflicts.

    Name Mangling:- interpreter of the Python alters the variable name in a way that it is challenging to clash when the class is inherited.

"""

class Sample():

    def __init__(self):
        self.a = 1
        self._b = 2
        self.__c = 3
obj1 = Sample()
dir(obj1)


"""
['_Sample__c',
 '__class__',
 '__delattr__',
 '__dict__',
 '__dir__',
 '__doc__',
 '__eq__',
 '__format__',
 '__ge__',
 '__getattribute__',
 '__gt__',
 '__hash__',
 '__init__',
 '__init_subclass__',
 '__le__',
 '__lt__',
 '__module__',
 '__ne__',
 '__new__',
 '__reduce__',
 '__reduce_ex__',
 '__repr__',
 '__setattr__',
 '__sizeof__',
 '__str__',
 '__subclasshook__',
 '__weakref__',
 '_b',
 'a']


The above code returns all the attributes of the class object. Let's see our variables in the attributes list.

self.a variable appears in the list without any change.

self._b Variable also appears in the list without any change. As we discussed above, it's just for the internal use.

    Is there self.__c variable in the list?
        If you carefully look at the attributes list, you will find an attribute called _Sample__c. This is the name mangling. It is to avoid the overriding of the variable in subclasses.

Let's create another class by inheriting Sample class to see how overriding works.
"""

class SecondClass(Sample):

    def __init__(self):
        super().__init__()
        self.a = "overridden"
        self._b = "overridden2"
        self.__c = "overridden3"
obj2 = SecondClass()
print(obj2.a)
print(obj2._b)
# print(obj2.__c)  # dessa forma gera erro

print(obj2._SecondClass__c)

# See, it's worked you can also access the previously
# created variable using _Sample__c. Let's see
print(obj1._Sample__c)


"""
You can access the Double Pre Underscore variables using methods in the class. Let's see an example.
"""
class SimpleClass:

    def __init__(self):
        self.__datacamp = "Excellent"

    def get_datacamp(self):
        return self.__datacamp



obj = SimpleClass()
print(obj.get_datacamp()) ## it prints the "Excellent" which is a __var
# print(obj.__datacamp)     ## here, we get an error as mentioned before. It changes the name of the variable
print(obj._SimpleClass__datacamp)     ## here, we get an error as mentioned before. It changes the name of the variable



class SimpleClass2:

    def __datacamp(self):
        return "datacamp"

    def call_datacamp(self):
        return self.__datacamp()


obj2 = SimpleClass2()
print(obj2.call_datacamp()) ## same as above it returns the Dobule pre underscore method
# print(obj2.__datacamp())    ## we get an error here
print(obj2._SimpleClass2__datacamp())    ## we get an error here


"""
Let's look at the name mangling in another way. First, we will create a variable with name _SimpleClass__name, and then we will try to access that variable using Doble Pre Underscore name.
"""

_SimpleClass3__name = "datacamp3"

class SimpleClass3:

    def return_name(self):
        return __name

obj3 = SimpleClass3()
print(obj3.return_name()) ## it prints the __name variable


"""
5.4. Double Pre And Post Underscores

__name__

In Python, you will find different names which start and end with the double underscore. They are called as magic methods or dunder methods.
"""

class Sample():

    def __init__(self):
        self.__num__ = 7

obj4 = Sample()
print(obj4.__num__)
