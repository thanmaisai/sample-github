# this file consists an error in elsif ans else statement
a = int(input('Enter first number  : '))
b = int(input('Enter second number : '))
c = int(input('Enter third number  : '))

largest = 0

if a > b and a > c :
    largest = a
elif b > c and b > a:
    largest = b #b
else :
    largest = c #c

print(largest, "is the largest of three numbers.")
