#print_statement
#print("I love pizza")
#print("It's really good")

#String_datatype
first_name = "Joe"
last_name = "Dow"
#print(type(first_name))
#print("Hello "+first_name)
#print("Hello " + first_name + " " + last_name)

#integer_datatype
age = 19
age = age + 1
age += 1
#print("My age is " + str(age))#change to string then only concatenate, cant concatenate string to integer
#print(type(age))#print data type of variable age

#float_datatype
height = 250.5
#print(height)
#print(type(height))
#print("Your height is " + str(height) + " cm")

#boolean_datatype
human = True
#print(human)
human = False
#print(human)
#print(type(human))
#print("Are you a Human: " + str(human))

#mutiple_assignment
name = "Bro"
age = 21
attractive = True
#print(name)
#print(age)
#print(attractive)
name, age, attractive = "Bros", 34, False#multiline initialization
#print(name)
#print(age)
#print(attractive)
a = b = c = d = 30#if all variables have equal value
#print(a)
#print(b)
#print(c)
#print(d)

#String_methods
name = "priyam"
#print(len(name))#find length of string
#print(name.find("r"))#find index of "r" in the string
#print(name.find("R"))#if index not found returns -1
#print(name.capitalize())#make only the first letter capital
#print(name.upper())#to upper case
#print(name.lower())#to lower case
#print(name.upper())
#print(name)#original string is not modified
#print(name.isdigit())#check if the string is digit or number
#print(name.isalpha())#check if string has only alphabets and no space or special characters
#print(name.count("i"))#count number of "i"'s in the string
#print(name.replace("i","o"))#replace all "i"'s with "o"'s
#print(name*3)#print the same string 3 times, not a method but a useful feature

#type_casting-convert one data type to another
x = 1
y = 2.0
z = "3"

#print(x)
#print(int(y))#only temporary, value of y is still 2.0
#print(z)

y = int(y)#float to int
#print(y)

#print(z*3)
z = int(z)#string to int
#print(z)
#print(z*3)

x = float(x)#int to float
#print(x)

y = str(y)#int to string
#print(y)
#int to str is used within print satements that concatenate string and integer

#accept user input
#name = input("What is your name: ")#input function is used, takes input only as a String
#age = int(input("How old are you: "))#for other types we have to typecast
#age = age + 1
#print("Hello " + name)
#print("You are " + str(age) + " years old.")#while printing remeber to typecast again
#height = float(input("How tall are you: "))#python does not support concept of data loss i.e. float String be stored in int, float string can only be stored in a float type
#print("You are " + str(height) + " cm tall")

#math functions
import math#math class contains all built-in mathematical functions

pi = 3.14
#print(round(pi))#round function rounds off variable or value to the nearest whole integer
#print(math.ceil(pi))#round up i.e. next
#print(math.floor(pi))#round down i.e. previous
#print(abs(pi))#find absolute or mod value(+ve value)
#print(pow(pi,2))#raise pi to the 2nd power
#print(math.sqrt(pi))#find the square root of pi
#print(max(1, 5, 4))#finds the maximum among a set of variables or values
#print(min(4, -1 ,7))#finds the minimum among a set of variables or values

#String Slicing--create a substring, we can use indexing[] or slice()
#indexing[]--[start:stop:step]
name = "Bro Code"
first_name = name[0]#just giving the start index will give you only the character at that index
#print(first_name)#prints just 'B'
second_name = name[0:2]#gives only "Br" as stop index is exclusive while start index is inclusive
#print(second_name)
third_name = name[0:3]#or name[:3] is also the same
#print(third_name)
last_name = name[4:8]#from index 4 to 7, also name[4:] is also the same
#print(last_name)
#step is the value by which we increase our indexes between starting and stopping
funky_name = name[0:8:2]#or name[::3]
#print(funky_name)
#reverse a string
reversed_name = name[::-1]#giving a step of -1 will read the string backwards therefore reversing it
#print(reversed_name)

#slice() function
website1 = "http://google.com"
website2 = "http://wikipedia.com"
slice_obj = slice(7,-4)#creation of a reusable slice object; last character has index -1, second last has -2 and so on......we can utilize this to specify index of the '.', remember that '.' is exclusive
#print(website1[slice_obj])#now use the slice object created with your string is index form
#print(website2[slice_obj])#resuability

#if statement
#age = int(input("How old are you?: "))
#if age >= 18:
    #print("You are legally an adult")
#elif age < 0:
    #print("you haven't been born yet")
#elif age == 100:
    #print("You are God")
#else:
    #print("You are not an adult")

#logical operators
#temp = int(input("What is the temperature outside?: "))
#if temp >= 0 and temp <= 30:
    #print("Nice weather Bro")
#elif temp > 30 and temp <= 50:
    #print("Extremely Hot")
#elif temp > 50 or temp < 0:
    #print("Unbearable")

#while loop
#name = ""#take name as empty string
#while len(name) == 0:#till you dont enter the name
    #name = input("Enter your name: ")#keep asking for the name
#print("Hello " + name)

#name2 = None#take name2 as None type, None is not the same as 0, False, or an empty string
#while not name2:#not None something and something in conditional statemets is true, except 0
    #name2 = input("Enter your name: ")#when you enter a name finally, not of that string will be false
#print("Hello " + name2)
#"Truthiness" of '', [], 0, {}, None

#for loop
#for i in range(50,100):#i is the loop variable, no need to declare it. Range() is the range over which loop runs. Remember in range(a,b), a is inclusive and b is exclusive
    #print(i+1)
#for i in range(50,100,2):#3rd argument is the step
    #print(i)
#for i in "Priyam Verma":
    #print(i)

import time#time module has sleep function
#for seconds in range(10,0,-1):#from 10 to 0(exclusive) decremeting by 1
    #print(seconds)
    #time.sleep(1)#after each second printing, wait for 1 second before looping back
#print("Happy New Year")

#nested loops
#rows = int(input("How many rows?:"))
#columns = int(input("How many columns?: "))
#symbol = input("Enter a symbol to use: ")

#for i in range(rows):#outer loop
    #for j in range(columns):#inner loop
        #print(symbol, end="")#print symbol in row
    #print()#change line

#Loop control statements
#break : Used to terminate the loop entirely
#continue : Skips the iteration of the loop
#pass : Does nothing, acts as a placeholder
#while True:
    #name = input("Enter your name: ")
    #if name != "":
        #break

#phone_number = "987-654-3210"
#for i in phone_number:
    #if i == "-":
        #continue
    #print(i, end = "")

#for i in range(1,21):
    #if i == 13:
        #pass
    #else:
        #print(i)

#Lists : Used to store multiple items in a single variable
food = ["pizza","hamburger","hotdog","spaghetti"]#a list
food[0] = "sushi"#change first element from "pizza" to "sushi"
#print(food[2])#"hotdog"
#print(food[0])#"sushi"
#for x in food:#method to print all elements of a list
    #print(x)

food.append("ice cream")#add "ice cream" at the end of list
#print(food)
food.remove("hotdog")#remove the element specified i.e. "hotdog"
#print(food)
food.pop()#remove the last element of the list
#print(food)
food.insert(0,"cake")#insert "cake" at the index 0
#print(food)
food.sort()#"sort the list in alphabetical order
#print(food)
food.clear()#"clear the complete list i.e. all elemets become null"
#print(food)

#2D Lists - A list of lists
drinks = ["coffee","soda","tea"]
dinner = ["pizza","hamburger","hotdog"]
dessert = ["cake","ice cream"]

food = [drinks,dinner,dessert]#list of lists
#print(food)#print whole food
#print(food[1])#print only drinks
#print(food[1][2])#print 3rd element of 2nd list i.e. hotdog of list dinner

#Tuple - collection whicj is ordered and unchangable
#        used to group together related data
student = ("Bro",21,"male")#use () in place of [] as in list
#print(student.count("Bro"))#count and print the number of appearances of "Bro" in student
#print(student.index("male"))#report the inndex of "male" in student

#for x in student:#method to print all the elements of a tuple
    #print(x)

#if "Bro" in student:#check if "Bro" is an element of tuple student
    #print("Bro is here")

#Set - collection which is unordered, unindexed. No duplicate values
utensils = {"fork","spoon","knife","spoon","spoon"}#use {}, only one "spoon" will be printed as no duplicate values are allowed
dishes = {"bowl","plate","cup","knife"}
#for x in utensils:#method to print set elements
    #print(x)
#a set is faster than a list if we want to perform a linear search due to its unorderness
#utensils.add("napkin")#add the element "napkin" to the set utensils
#print(utensils)
utensils.remove("fork")#remove the element "fork" in the set utensils
#print(utensils)
utensils.update(dishes)#this will add all the elements of the set dishes to the set utensils
#print(utensils)
dinner_table = utensils.union(dishes)#add two sets to make a new set
#print(dinner_table)
#print(utensils.difference(dishes))#print elements that are present in utenils but not in dishes
#print(utensils.intersection(dishes))#print elemsnts that common to both utensils and dishes

#dictionary - A changeable, unordered collection of unique key:value pairs
#             Fast because they use hashing, allow us to access a value quickly
