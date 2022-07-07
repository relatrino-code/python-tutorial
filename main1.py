import ast
from itertools import count
import string


print("This is going to be printed")
# The print function simply prints output the screen
x = 1
# No need to specify the type of variable
if x == 2:
    # indentation of a tab or 4 spaces specifies a block of code, : is used to start a block of code
    print("x is not 1")
else:
    print("x is equal to 1")
print("Hello, World!")
myint = 7  # integer type variable myint
print(myint)
myfloat = 6.0  # float type variable myfloat
print(myfloat)
# the float function will convert integer to floating value
myfloat = float(55)
print(myfloat)
# Strings can be defined either with '' or with ""
mystring = 'Hello, World!'
print(mystring)
mystring = "Hello, World!"
print(mystring)
one = 1
two = 2
three = one + two  # simple mathematical addition
print(three)
hello = "Hello"
world = "World"
helloworld = hello + ", " + world + "!"  # string concatenation
print(helloworld)
a, b = 3, 4  # assignments on more than one variable simultaneously
print(a, b)  # printing two variables simultaneously
# We should note that we cannot add a number to a string
# printing can be done via placeholder as in C
print("String is : %s" % hello)
# the isinstance function tests a variable for a given data type
if isinstance(myfloat, float):
    print("Float is : %f" % myfloat)
# Lists are similar to arrays, contain one type of variable and as many variables as we want
mylist = []  # initializing th list with nothing
# to add a value to the list we use the append() function
mylist.append(1)  # added value 1 to the first element of list
mylist.append(10)  # added value 10 to the second element of list
mylist.append(100)  # added value 100 to the third element of list
mylist.append(1000)
# indexing starts from 0 and represenation of each element is like an array.
print(mylist[3])
print(mylist[1])
# to print the whole list just iterate over it
for i in mylist:
    print(i)
# if we print the list name itself it would include the []
print(mylist)
numbers = []
strings = []
names = ["John", "Eric", "Jessica"]  # names list is initialized with 3 names
numbers.append(1)
numbers.append(2)
numbers.append(3)
strings.append('hello')
strings.append('world')
# storing element 2 of names list to second_name variable
second_name = names[1]
print(numbers)
print(strings)
print("The second name on the names list is %s" % second_name)
# Arithmetic operations can be performed on numbers
# python follows the order of operations in mathematics i.e. *, /, % before +, -
num = 1 + 2 * 3 / 4.0
print(num)
remainder = 11 % 3  # % returns the remainder of division
print(remainder)
squared = 7 ** 2  # using two multiplication symbols makes a power relationship
print(squared)
cubed = 2 ** 3
print(cubed)
# Using operators with strings
print('hello' + 'world')  # + operator can also be used to concatenate strings
# multiplying a string with number forms a string with that many substrings
lotsofhellos = "hello" * 10
print(lotsofhellos)
# Using operators with lists
even_numbers = [2, 4, 6, 8]
odd_numbers = [1, 3, 5, 7]
# two lists can be combined using the + operator
all_numbers = odd_numbers + even_numbers
print(all_numbers)
# the * operator produces more subsequences of the original in a list
print([1, 21, 3] * 3)
# the len() function tells us the length of a list
x = object()
y = object()
x_list = [x] * 10
y_list = [y] * 10
big_list = x_list + y_list
print("x_list contains %d elements" % len(x_list))
print("y_list contains %d elements" % len(y_list))
print("big_list contains %d elements" % len(big_list))
# The count(value) function counts the number of occureneces of a value in a list
if x_list.count(x) == 10 and y_list.count(y) == 10:
    print("Almost there...")
if big_list.count(x) == 10 and big_list.count(y) == 10:
    print("Great!")
# String Formatting
myname = "Relatrino"
print("Hello, %s!" % myname)
myage = 20
print("%s is %d years old." % (myname, myage))
# An object that is not a string can also be printed using %s.
mylists = [1, 2, 3]
print("My list is as follows %s" % mylists)
# Some basic argument specifiers :
# %s - String(or any object with string representation)
# %d - Integers
# %f - Floating point numbers
# %.<number of digits>f - Floating point numbers with a fixed amount of digits to the right of the decimal point
# %x/%X - Integers in hex represenation
data = ("John", "Doe", 53.44)
mystr = "Hello %s %s. Your current balance is $%.2f"
print(mystr % data)
# Basic String Operations
astring = "Hello World!"
print(len(astring))  # len() returns the length of the inputed string
print("These are single quotes -> ''")
# index() returns the first appeared/starting index of the character/substring inputed
print(astring.index("o"))
# count() returns the number of times a particular character/substring appeares in a string
print(astring.count("l"))
# [index1:index2] cuts a substring from index1 upto (index2)-1
print(astring[3:8])
print(astring[3])  # just an index will cut the character at that index
print(astring[3:])  # first index and : cuts from index to end of string
# : and last index cuts from start of string to (last index)-1
print(astring[:8])
# Last character has index len-1 or -1 similarly second last has -2 so we can feed negative numbers in [:] to cut from backwards to forward
print(astring[3:-7])  # Here both indexes are inclusive
# cuts from 3 to 7 but leaving one character as step is 2, so every alternate character. By default the value is 1.
print(astring[3:8:2])
# This is extended slice syntax -> [start:stop:step]
# We can reverse a string using this
print(astring[::-1])
print(astring.upper())  # Converts all letters to uppercase
print(astring.lower())  # Converts all letters to lowercase
# Returns truue or false dependig on whether astring starts with "Hello"
print(astring.startswith("Hello"))
# Returns truue or false dependig on whether astring ends with "wod!"
print(astring.endswith("wod!"))
# Splits the string at the specified chaaracter/substring, stores it in a list and excludes the character/substring inputed
afewwords = astring.split("Wo")
print(afewwords)
s = "My length is twenty!"
print("Length of s = %d" % len(s))
print("The first occurence of character e is = %d" % s.index("e"))
print("e occures %d times" % s.count("e"))
print("The first five characters are '%s'" % s[:5])
print("The next five characters are '%s'" % s[5:10])
print("The thirteenth character is '%s'" % s[12])
print("The characters with odd index are '%s'" % s[1::2])
print("The last five characters are '%s'" % s[15:])
print("String in UPPERCASE '%s'" % s.upper())
print("String in lowercase '%s'" % s.lower())
if s.startswith("My l"):
    print("String starts with 'My l'. Good!")
else:
    print("Bad!")
if s.endswith("ty"):
    print("String ends with 'ty'. Good!")
else:
    print("Bad!")
print("Split the words of the string : %s" % s.split(" "))
# Conditionals
xo = 2
print(xo == 2)  # copparision for equality
print(xo == 3)
print(xo < 3)  # comparision for less than
# Boolean Operators
namemy = "Relatrino"
agemy = 20
if namemy == "Relatrino" and agemy == 20:
    print("Your name is Relatrino, and you are 20 years old.")
if namemy == "Relatrino" or namemy == "Rick":
    print("Your name is either Relatrino or Rick.")
# 'in' operator checks whether a specified object exists within an iterable object container, like a list
testname = "Joe"
if testname in ["John", "Joe", "Rick"]:
    print("Congrats, the name you entered was found in the database")
else:
    print("Sorry, inputed name not found in database")
statement = True
if statement is False:
    print("Authentication failed, we'll have to terminate you.")
elif statement is True:
    print("Authentication Successful")
#The 'is' operator is used to check whether 2 objects are identical or not and return a boolean value
#There can be 2 cases when an if statement passes, either the condition returns true or an non empty object is passed.
#Empty objects : "", [], 0, False
#Unlike the '==' operator, the 'is' operator does not match the values of the variables, but the instances themselves.
xy = [1, 2, 3]
za = [1, 2, 3]
print(xy == za)#prints true
print(xy is za)#prints false
#The 'not' operator before a boolean expression inverts it
print(not False)#prints True
first_number = 16
second_number = 0
first_array = [1,2,3]
second_array = [1,2]
if first_number > 15:
    print("1")
if first_array:
    print("2")
if len(second_array) == 2:
    print("3")
if len(first_array) + len(second_array) == 5:
    print("4")
if first_array and first_array[0] == 1:
    print("5")
if not second_number:
    print("6")
#Loops
#For Loop : Iterates over  a given sequence
print("For Loops")
primes = [2, 3, 5, 7, 9]
for i in primes:
    print(i)
#For loops iterate over a sequence of numbers using range and xrange functions
#Range returns a new list with numbers of that specified range  while xrange returns an iterator which is more efficient
#range is a 0 based function
for x in range(5):
    print(x)
for x in range(3, 6):
    print(x)
#Hence we see that the outer number is exclusive
for x in range(3, 8, 2):
    print(x)
#range(start(inclusive), stop(exclusive), step)
#While Loop : Iterate as long a s a given boolean expression is True
print("While Loops")
counta = 0
while counta < 5:
    print(counta)
    counta += 1#counta = counta + 1
#Break and Continue
#break statement : used to exit a for or a while loop
#continue : skips the current block and skips to the for or while block
print("Break Statement")
countb = 0
while True:
    print(countb)
    countb += 1
    if countb >= 5:
        break
print("Continue Statement")    
for x in range(10):
    if x % 2 == 0:
        continue
    print(x)
#'else' for loops : We can use else for loops which is executed when the loop condition fails. But else is not executed when a break statement is executed inside loop.
print("else in loops part1")
countc = 0
while countc < 5:
    print(countc)
    countc += 1
else:
    print("countc variable has reached value %d" % countc) 
print("else in loops part2")
for xt in range(1,10):
    if(xt % 5 == 0):
        break
    print(xt)
else:
    print("This statement will not be executed as loop is terminated due to break and not due to loop condition fail")   
#Functions : Functions are a convenient way to divide your code into useful blocks, allowing us to order our code, make it more readable, reuse it and save some time. Also functions are a key way to define interfaces so programmers can share their code.
#Functions in python are defined using the block keyword "def", followed with the function's name as the block's name.
print("Functions")
def my_function():
    print("This is my Funtion!")
#Functions may also receive arguments (variables passed from the caller to the function).
def my_function_with_args(username, greeting):
    print("Hello %s, from My Function!, I wish you %s" % (username, greeting))
#Functions may return a value to the caller, using the keyword- 'return'.
def sum_two_numbers(a, b):
    return a + b
#Calling Functions
#Write the function's name followed by () , placing arguments within brackets
my_function()
my_function_with_args("Relatrino", "a great year!")
print(sum_two_numbers(1, 2))
def benefit_strings(benefit):
    return "%s is a good person." % benefit
print(benefit_strings("Relatrino"))  
#Classes and Objects
#Objects are an encapsulation of variables and functions into a single entity.
#Objects get their variables and functions from classes. Classes are essentially a template to create your objects.
print("Here comes a class:")
class MyClass:
    myVariable = "Blah"
    def myFunction(self):
        print("My name is Relatrino!")        
#How to assign a class template to an object?
myObject = MyClass()
#Now the variable "myObject" holds an object of the class "MyClass" that contains the variable and the function defined within the class called "MyClass".
#Accessing Object Variables:
print(myObject.myVariable)
myObject1 = MyClass()
myObject1.myVariable = "Hehe"#changing the value of the variable myVariable for the myObject1 object.
print(myObject1.myVariable)
print(myObject.myVariable)#Changing the variable for one object does not affect another object, eac object has independent copies of the same variables and  functions.
myObject.myFunction()#Accessing Object Functions
#The __init__() function : A special function called when the class is being initiated. Used for assigning values in a class.
class NumberHolder:
    def __init__(self, number):
        self.number = number
    def returnNumber(self):
        return self.number
var = NumberHolder(7)
print(var.returnNumber())
#EXAMPLE:
class Vehicle:
    def __init__(self, name, kind, color, value):
        self.name = name
        self.kind = kind
        self.color = color
        self.value = value
    def description(self):
        desc_str = "%s is a %s %s worth $%.2f." % (self.name, self.kind, self.color, self.value)
        return desc_str

car1 = Vehicle("Fer", "convertible", "red", 60000)
car2 = Vehicle("Jump", "van", "blue", 10000)
print(car1.description())
print(car2.description())
#Dictionaries:
print("Here come the Dictionaries:")
#A dictionary is a data type similar to arrays, but works with keys and values instead of indexes.
#Each value stored in a dictionary can be accessed using a key, which is any type of object (a string, a number, a list, etc.) instead of using its index to address it.
phonebook = {}
phonebook["Relatrino"] = 1234567890
phonebook["Joe"] = 1234567890
phonebook["Deckard"] = 1112223330
phonebook["Luv"] = 9876543210
print(phonebook)
#Another way to initialize a dictionary:
directory = {
    "Documents" : 63.7,
    "Downloads" : 123.4,
    "Pictures" : 98.2,
    "Music" : 21.1
}
print(directory)
#Iteration over Dictionaries is done using the items() function
for x, i in phonebook.items():
    print("phone number of %s is %d" % (x, i))
#A list is ordered whereas a dictionary is unordered
#To delete an item in a dictionary, we either use del or pop()
del phonebook["Relatrino"]
directory.pop("Downloads")
print(phonebook)
print(directory)
phonebook["Relatrino"] = 4564564567
if "Relatrino" in phonebook:
    print("Relatrino is here!")
if "Downloads" not in directory:
    print("Downloads have been removed!")
print(phonebook)
print(directory)
#Modules and Packages:
print("Here come Modules and Packages:")
#Modules in Python are just Python files with a .py extension. The name of the module is the same as the file name.
#A Python module can have a set of functions, classes, or variables defined and implemented.
#Modules are imported from other modules using the import command.
#To use a funtion implemeted in a module somewhere, we will use the dot(.) operator to specify which module the function is implemented, like module_name.function_name()
#When we use the import command to import a module, python looks for the module's .py file in the directory where the script was executed. There are also built-in modules.
#When importing a module, a .pyc file is created. This is a compiled Python file. Python compiles files into Python bytecode so that it won't have to parse the files each time modules are loaded.
#If a .pyc file exists, it gets loaded instead of the .py file.
#If we do not want to use the (.) operator for referencing all the time, we can use the the from command to import all or specific objects from a module
#For importinf all objects from a module use : from module_name import *
#For importing just a specific function or object use : from module_name import function_name
#A namespace is a system where every object is named and can be accessed in Python.
#Custom Import Names : Modules can be imported under any name we want using : import module_name as custom_module_name
#Module Initialization : The first time a module is loaded into a running Python script, it is initialized by executing the code in the module once.
#If another module in your code imports the same module again, it will not be loaded again, so local variables inside the module act as a "singleton," meaning they are initialized only once.
#Extending Module Load Path : There are a couple of ways to tell the Python interpreter where to look for modules, aside from the default local directory and built-in modules.
#1st way : You can use the environment variable PYTHONPATH to specify additional directories to look for modules : PYTHONPATH=/directory python module_name.py
#2nd way : You may also use the sys.path.append function. Execute it before running the import command : sys.path.append("/directory")
#To import the module urllib, which enables us to create read data from URLs, we import the module : import urllib
#To use the urllib module : urllib.urlopen(...)
#We can look for what all functions are implemented in a module using the dir() function : dir(urllib)
#When we find the function in the module we want to use, we can read more about it with the help function, using the Python interpreter : help(urllib.urlopen)
#Writing Pakages : Packages are namespaces containing multiple packages and modules. They're just directories, but with certain requirements.
#Each package in Python is a directory which MUST contain a special file called __init__.py. This file, which can be empty, indicates that the directory it's in is a Python package. That way it can be imported the same way as a module.
#If we create a directory called foo, which marks the package name, we can then create a module inside that package called bar. Then we add the __init__.py file inside the foo directory.
#To use the module bar, we can import it in two ways :
#Way 1 : import foo.bar(we will have to use foo prefix whenever we access the module bar)
#Way 2 : from foo import bar(no need to use the foo prefix aswe have imported the module to our module's namespace)
#The __init__.py file can also decide which modules the package exports as the API, while keeping other modules internal, by overriding the __all__ variable : __all__ = ["bar"]
#Print an alphabetically sorted list of all the functions in the re module containing the word find:
import re
find_members = []
for member in dir(re):
    if "find" in member:
        find_members.append(member)
print(sorted(find_members))














