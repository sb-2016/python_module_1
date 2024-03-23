#!/bin/bash

# Introduction to Python

echo "Hello world"

carlist=("Honda" "Toyota" "Mahindra")
for car in "${carlist[@]}"; do
    echo "$car"
done

# Variables
name='Swarnendu '
age=27
echo "$name"Who age is "$age"
echo "${name}who age is ${age}"

# Arithmetic Operator
# + - * / % ** //
a=$((2 + 8))
b=$((8 - 3))
c=$((2 * 8))
d=$((8 / 2))
e=$((8 % 3))
f=$((2 * (2 + 8)))
echo "$a"
echo "$b"
echo "$c"
echo "$d"
echo "$e"
echo "$f"

# Calculator
read -p "Enter first number : " a
read -p "Enter second number : " b
echo "Addition : $((a + b))"
echo "Subtract : $((a - b))"
echo "Multiply : $((a * b))"
echo "Division : $((a / b))"
echo "Remainder : $((a % b))"
echo "Exponent : $((a ** b))"
echo "Floor Division : $((a / b))"

# Comparison Operator
# == != > < >= <=
a=2
b=3
c=2
d=3
echo "$((a == b))"
echo "$((a != b))"
echo "$((a > b))"
echo "$((a < b))"
echo "$((a >= b))"
echo "$((a <= b))"
echo "$((a == c))"
echo "$((a != c))"
echo "$((a > c))"
echo "$((a < c))"
echo "$((a >= c))"
echo "$((a <= c))"
echo "$((b == d))"
echo "$((b != d))"
echo "$((b > d))"
echo "$((b < d))"
echo "$((b >= d))"
echo "$((b <= d))"

# Logical Operator
# and or not
a=2
b=3
c=2
d=3
echo "$((a == b && a == c))"
echo "$((a == b || a == c))"
echo "$((! (a == b)))"
echo "$((! (a == c)))"

# Assignment Operator
# = += -= *= /= %= **= //=
a=2
b=3
a=$((a + b))
echo "$a"
a=$((a - b))
echo "$a"
a=$((a * b))
echo "$a"
a=$((a / b))
echo "$a"
a=$((a % b))
echo "$a"
a=$((a ** b))
echo "$a"
a=$((a / b))
echo "$a"

# Operators
# Weather condition
weather_condition="rainy"
if [ "$weather_condition" = "rainy" ]; then
    echo "Take umbrella"
elif [ "$weather_condition" = "sunny" ]; then
    echo "Take sunglasses"
else
    echo "Take nothing"
fi

# Functions
# Greetings Function
greetings() {
    local name="$1"
    echo "Hello $name How are you?"
}

greetings 'Swarnendu'

# Calculate area of a rectangle function
area_of_rectangle() {
    local length="$1"
    local width="$2"
    local area=$((length * width))
    echo "Area of rectangle is $area"
}

area_of_rectangle 10 20

# Withdraw money function
withdraw_money() {
    local balance="$1"
    local amount="$2"
    if [ "$amount" -gt "$balance" ]; then
        echo "Insufficient balance"
    else
        balance=$((balance - amount))
        echo "Remaining balance is $balance"
    fi
}

withdraw_money 1000 500

# Loops
# For loop
for ((i = 1; i <= 10; i++)); do
    echo "this is a loop$i"
done

# While loop
i=1
while [ "$i" -le 10 ]; do
    echo "this is a loop$i"
    ((i++))
done

# Decrement while loop
i=10
while [ "$i" -ge 1 ]; do
    echo "this is a loop$i"
    ((i--))
done

# Modules
# Importing modules
echo "sqrt(16)" | bc -l
echo "Hello"
sleep 2
echo "World"
echo "$((RANDOM % 10 + 1))"

# Calculate area of a rectangle function
area_of_rectangle() {
    local length="$1"
    local width="$2"
    local area=$((length * width))
    echo "Area of rectangle is $area"
}

# Calculate area of a circle function
area_of_circle() {
    local radius="$1"
    local area=$(echo "scale=2; 3.14 * $radius * $radius" | bc -l)
    echo "Area of circle is $area"
}

source area_of_shapes.sh

area_of_rectangle 10 20
area_of_circle 10

# List
carlist=("Honda" "Toyota" "Mahindra")
echo "${carlist[@]}"
echo "${carlist[0]}"
echo "${carlist[1]}"
echo "${carlist[2]}"
echo "${carlist[@]:0:2}"
echo "${carlist[@]:0:3}"
echo "${carlist[@]:0}"
echo "${carlist[@]:0:2}"
echo "${carlist[@]}"
carlist+=("Tata")
echo "${carlist[@]}"
carlist[1]="Suzuki"
echo "${carlist[@]}"
unset 'carlist[0]'
echo "${carlist[@]}"
carlist[0]="Hyundai"
echo "${carlist[@]}"
for car in "${carlist[@]}"; do
    echo "$car"
done

# Dictionary
declare -A car_dict=(
    ["Brand"]="Honda"
    ["Model"]="Civic"
    ["Year"]="2022"
)

echo "${car_dict["Brand"]}"
echo "${car_dict["Model"]}"
echo "${car_dict["Year"]}"

Brand="${car_dict["Brand"]}"
echo "$Brand"

keys="${!car_dict[@]}"
echo "$keys"

car_dict["Brand"]="Toyota"
echo "${car_dict["Brand"]}"

car_dict["Year"]="2023"
echo "$keys"
echo "${car_dict["Year"]}"
#!/bin/bash

# Introduction to Python

echo "Hello world"

carlist=("Honda" "Toyota" "Mahindra")
for car in "${carlist[@]}"; do
    echo "$car"
done

# Variables
name='Swarnendu '
age=27
echo "$name"Who age is "$age"
echo "${name}who age is ${age}"

# Arithmetic Operator
# + - * / % ** //
a=$((2 + 8))
b=$((8 - 3))
c=$((2 * 8))
d=$((8 / 2))
e=$((8 % 3))
f=$((2 * (2 + 8)))
echo "$a"
echo "$b"
echo "$c"
echo "$d"
echo "$e"
echo "$f"

# Calculator
read -p "Enter first number : " a
read -p "Enter second number : " b
echo "Addition : $((a + b))"
echo "Subtract : $((a - b))"
echo "Multiply : $((a * b))"
echo "Division : $((a / b))"
echo "Remainder : $((a % b))"
echo "Exponent : $((a ** b))"
echo "Floor Division : $((a / b))"

# Comparison Operator
# == != > < >= <=
a=2
b=3
c=2
d=3
echo "$((a == b))"
echo "$((a != b))"
echo "$((a > b))"
echo "$((a < b))"
echo "$((a >= b))"
echo "$((a <= b))"
echo "$((a == c))"
echo "$((a != c))"
echo "$((a > c))"
echo "$((a < c))"
echo "$((a >= c))"
echo "$((a <= c))"
echo "$((b == d))"
echo "$((b != d))"
echo "$((b > d))"
echo "$((b < d))"
echo "$((b >= d))"
echo "$((b <= d))"

# Logical Operator
# and or not
a=2
b=3
c=2
d=3
echo "$((a == b && a == c))"
echo "$((a == b || a == c))"
echo "$((! (a == b)))"
echo "$((! (a == c)))"

# Assignment Operator
# = += -= *= /= %= **= //=
a=2
b=3
a=$((a + b))
echo "$a"
a=$((a - b))
echo "$a"
a=$((a * b))
echo "$a"
a=$((a / b))
echo "$a"
a=$((a % b))
echo "$a"
a=$((a ** b))
echo "$a"
a=$((a / b))
echo "$a"

# Operators
# Weather condition
weather_condition="rainy"
if [ "$weather_condition" = "rainy" ]; then
    echo "Take umbrella"
elif [ "$weather_condition" = "sunny" ]; then
    echo "Take sunglasses"
else
    echo "Take nothing"
fi

# Functions
# Greetings Function
greetings() {
    local name="$1"
    echo "Hello $name How are you?"
}

greetings 'Swarnendu'

# Calculate area of a rectangle function
area_of_rectangle() {
    local length="$1"
    local width="$2"
    local area=$((length * width))
    echo "Area of rectangle is $area"
}

area_of_rectangle 10 20

# Withdraw money function
withdraw_money() {
    local balance="$1"
    local amount="$2"
    if [ "$amount" -gt "$balance" ]; then
        echo "Insufficient balance"
    else
        balance=$((balance - amount))
        echo "Remaining balance is $balance"
    fi
}

withdraw_money 1000 500

# Loops
# For loop
for ((i = 1; i <= 10; i++)); do
    echo "this is a loop$i"
done

# While loop
i=1
while [ "$i" -le 10 ]; do
    echo "this is a loop$i"
    ((i++))
done

# Decrement while loop
i=10
while [ "$i" -ge 1 ]; do
    echo "this is a loop$i"
    ((i--))
done

# Modules
# Importing modules
echo "sqrt(16)" | bc -l
echo "Hello"
sleep 2
echo "World"
echo "$((RANDOM % 10 + 1))"

# Calculate area of a rectangle function
area_of_rectangle() {
    local length="$1"
    local width="$2"
    local area=$((length * width))
    echo "Area of rectangle is $area"
}

# Calculate area of a circle function
area_of_circle() {
    local radius="$1"
    local area=$(echo "scale=2; 3.14 * $radius * $radius" | bc -l)
    echo "Area of circle is $area"
}

source area_of_shapes.sh

area_of_rectangle 10 20
area_of_circle 10

# List
carlist=("Honda" "Toyota" "Mahindra")
echo "${carlist[@]}"
echo "${carlist[0]}"
echo "${carlist[1]}"
echo "${carlist[2]}"
echo "${carlist[@]:0:2}"
echo "${carlist[@]:0:3}"
echo "${carlist[@]:0}"
echo "${carlist[@]:0:2}"
echo "${carlist[@]}"
carlist+=("Tata")
echo "${carlist[@]}"
carlist[1]="Suzuki"
echo "${carlist[@]}"
unset 'carlist[0]'
echo "${carlist[@]}"
carlist[0]="Hyundai"
echo "${carlist[@]}"
for car in "${carlist[@]}"; do
    echo "$car"
done

# Dictionary
declare -A car_dict=(
    ["Brand"]="Honda"
    ["Model"]="Civic"
    ["Year"]="2022"
)

echo "${car_dict["Brand"]}"
echo "${car_dict["Model"]}"
echo "${car_dict["Year"]}"

Brand="${car_dict["Brand"]}"
echo "$Brand"

keys="${!car_dict[@]}"
echo "$keys"

car_dict["Brand"]="Toyota"
echo "${car_dict["Brand"]}"

car_dict["Year"]="2023"
echo "$keys"
echo "${car_dict["Year"]}"
