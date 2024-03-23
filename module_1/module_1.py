# Introduction to Python
print('Hello world ')

carlist = ["Honda", "Toyota", "Mahindra"]
for car in carlist:
    print(car)
# Variable
name = 'Swarnendu '
age = 27
print(name + 'Who age is ' + str(age))
print(f'{name}who age is {age}')
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
# calculator
a = int(input("Enter first number : "))
b = int(input("Enter second number : "))
print(f'Addition : {a + b} \n'
      f'Subtact : {a - b} \n'
      f'Multiply : {a * b} \n'
      f'Devition : {a / b} \n'
      f'Remainder : {a % b} \n'
      f'Exponent : {a ** b} \n'
      f'Floor Division : {a // b}')
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
print(a == c)
print(a != c)
print(a > c)
print(a < c)
print(a >= c)
print(a <= c)
print(b == d)
print(b != d)
print(b > d)
print(b < d)
print(b >= d)
print(b <= d)
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
# operators
weather_condition = "rainy"
if weather_condition == "rainy":
    print("Take umbrella")
elif weather_condition == "sunny":
    print("Take sunglasses")
else:
    print("Take nothing")


# functions
# Greetings Function
def greetings(name):
    print(f'Hello {name} How are you?')


greetings('Swarnendu')


# Calculate area of a rectangle function
def area_of_rectangle(length, width):
    area = length * width
    print(f'Area of rectangle is {area}')


area_of_rectangle(10, 20)


# withdraw money function
def withdraw_money(balance, amount):
    if amount > balance:
        print("Insufficient balance")
    else:
        balance -= amount
        print(f'Remaining balance is {balance}')


withdraw_money(1000, 500)
# loops
# for loop
for i in range(1, 11):
    print('this is a loop' + str(i))
# while loop
i = 1
while i <= 10:
    print('this is a loop' + str(i))
    i += 1
# decrement while loop
i = 10
while i >= 1:
    print('this is a loop' + str(i))
    i -= 1
# modules
# importing modules
import math

print(math.sqrt(16))
import time
import random

### time modules example
print('Hello')
time.sleep(2)
print('World')
### random modules example
print(random.randint(1, 10))

import area_of_shapes as shapes

shapes.area_of_rectangle(10, 20)
shapes.area_of_circle(10)
# list
carlist = ["Honda", "Toyota", "Mahindra"]
print(carlist)
print(carlist[0])
print(carlist[1])
print(carlist[2])
# list slicing
print(carlist[0:2])
print(carlist[0:3])
print(carlist[0:])
print(carlist[:2])
print(carlist[:])
# list methods
carlist.append("Tata")
print(carlist)
carlist.insert(1,"Suzuki")
print(carlist)
carlist.remove("Honda")
print(carlist)
carlist[0] = "Hyundai"
print(carlist)
# list loops
for car in carlist:
    print(car)
# dictionary
car_dict = {
    "Brand": "Honda",
    "Model": "Civic",
    "Year": "2022"
}
print(car_dict["Brand"])
print(car_dict["Model"])
print(car_dict["Year"])
Brand = car_dict.get("Brand")
print(Brand)
keys = car_dict.keys()
print(keys)
car_dict["Brand"] = "Toyota"
print(car_dict["Brand"])
car_dict["Year"] = "2023"
print(keys)
print(car_dict["Year"])
