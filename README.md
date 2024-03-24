# Python Basics

This repository provides a collection of fundamental Python concepts and examples to help beginners understand basic programming principles using Python. Below are the key topics covered along with explanations and code examples.

## Introduction to Python

```bash
# Introduction to Python
print('Hello world ') # print statement

carlist = ["Honda", "Toyota", "Mahindra"] # list
for car in carlist: # for loop
    print(car) # print statement
```

The code above introduces basic Python syntax, including printing a string (`print()`), defining a list, and iterating over the elements of the list using a `for` loop.

## Variables

```bash
# Variable
name = 'Swarnendu ' # string variable
age = 27 # integer variable
print(name + 'Who age is ' + str(age)) # print statement
print(f'{name}who age is {age}')    # print statement
```

This section demonstrates the declaration and usage of variables in Python, including string concatenation and f-strings for formatting.

## Arithmetic Operators

```bash
# Arithmetic Operator
# + - * / % ** // 
a = 2 + 8 
b = 8 - 3 
c = 2 * 8
d = 8 / 2
e = 8 % 3
f = 2 * (2 + 8)
print(a)
print(b) 
print(c)
print(d)
print(e)
print(f)
```

Arithmetic operators such as addition, subtraction, multiplication, division, modulus, exponentiation, and floor division are demonstrated in this section.

## Calculator

```bash
# calculator
a = int(input("Enter first number : ")) # input statement
b = int(input("Enter second number : ")) # input statement
print(f'Addition : {a + b} \n' # print statement
      f'Subtact : {a - b} \n' # print statement
      f'Multiply : {a * b} \n'
      f'Devition : {a / b} \n'
      f'Remainder : {a % b} \n'
      f'Exponent : {a ** b} \n'
      f'Floor Division : {a // b}')
```

This section presents a basic calculator program that takes user input and performs arithmetic operations based on the input.

## Comparison Operators

```bash
# Comparison Operator
# == != > < >= <=
a = 2
b = 3
c = 2
d = 3
print(a == b)
print(a != b)
print(a > b)
print(a < b)
print(a >= b)
print(a <= b)
```

Comparison operators such as equal to, not equal to, greater than, less than, greater than or equal to, and less than or equal to are illustrated here.

## Logical Operators

```bash
# Logical Operator
# and or not
a = 2
b = 3
c = 2
d = 3
print(a == b and a == c)
print(a == b or a == c)
print(not (a == b))
print(not (a == c))
```

Logical operators including `and`, `or`, and `not` are demonstrated in this section.

## Assignment Operators

```bash
# Assignment Operator
# = += -= *= /= %= **= //=
a = 2
b = 3
c = 2
d = 3
a += b
print(a)
a -= b
print(a)
a *= b
print(a)
a /= b
print(a)
a %= b
print(a)
a **= b
print(a)
a //= b
print(a)
```

This section shows the usage of assignment operators such as `+=`, `-=`, `*=`, `/=`, `%=`, `**=`, and `//=`.

## Conditional Statements (if, elif, else)

```bash
# operators
weather_condition = "rainy"
if weather_condition == "rainy": # if statement
    print("Take umbrella")
elif weather_condition == "sunny": # else if statement
    print("Take sunglasses")
else:
    print("Take nothing") # else statement
```

This section demonstrates the usage of conditional statements (`if`, `elif`, and `else`) based on weather conditions.

## Functions

```bash
# functions
# Greetings Function
def greetings(name): # function
    print(f'Hello {name} How are you?') # print statement

greetings('Swarnendu') # function call
```

This section defines a simple greeting function and demonstrates its usage.

## Calculate Area of a Rectangle Function

```bash
# Calculate area of a rectangle function
def area_of_rectangle(length, width): # function
    area = length * width # calculation
    print(f'Area of rectangle is {area}') # print statement

area_of_rectangle(10, 20) # function call
```

A function to calculate the area of a rectangle is defined here, with an example of calling the function with specific length and width parameters.

## Withdraw Money Function

```bash
# withdraw money function
def withdraw_money(balance, amount): # function
    if amount > balance: # if statement 
        print("Insufficient balance") # print statement
    else: # else statement
        balance -= amount # calculation
        print(f'Remaining balance is {balance}') # print statement

withdraw_money(1000, 500) # function call
```

This section defines a function to withdraw money from an account, checking for sufficient balance, and updating the balance accordingly.

## Loops

```bash
# loops
# for loop
for i in range(1, 11):
    print('this is a loop' + str(i)) # print statement 
# while loop
i = 1   
while i <= 10: # while loop
    print('this is a loop' + str(i))
    i += 1
# decrement while loop
i = 10
while i >= 1: # while loop
    print('this is a loop' + str(i)) # print statement
    i -= 1
```

This section demonstrates `for` and `while` loops, including both incrementing and decrementing loops.

## Modules

```bash
# modules
# importing modules
import math # import statement

print(math.sqrt(16)) # print statement 
import time # import statement
import random # import statement

### time modules example 
print('Hello') 
time.sleep(2) 
print('World') 
### random modules example
print(random.randint(1, 10)) 

import area_of_shapes as shapes # import statement

shapes.area_of_rectangle(10, 20) # function call
shapes.area_of_circle(10) # function call
```

This section demonstrates importing and using modules such as `math`, `time`, and `random`, along with a custom module called `area_of_shapes`.

## Lists

```bash
# list
carlist = ["Honda", "Toyota", "Mahindra"] # list
print(carlist) 
print(carlist[0]) 
print(carlist[1])
print(carlist[2])
```

Lists and basic list operations like indexing and slicing

## Dictionaries

```bash
# dictionary
car_dict = { # dictionary
    "Brand": "Honda",
    "Model": "Civic",
    "Year": "2022"
}
print(car_dict["Brand"])
print(car_dict["Model"])
print(car_dict["Year"])
Brand = car_dict.get("Brand") # get method
print(Brand)
keys = car_dict.keys() # keys method
print(keys)
car_dict["Brand"] = "Toyota" # update method
print(car_dict["Brand"]) 
car_dict["Year"] = "2023" # update method
print(keys)
print(car_dict["Year"])
```

This section demonstrates dictionaries in Python, including creation, accessing values by keys, using the `get()` method, retrieving keys with `keys()`, and updating dictionary values.
