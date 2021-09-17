# Exercise 1
print("Hello world!")

# Exercise 2
print("Hell"+"o w"+"orld!")
# Not sure, so I'll write another variant
print("1")
print("2")
print("3")

# Exercise 3
print("Input square's width:")
width = float(input())
print("Input square's length:")
length = float(input())
print("Area of rectangle is: " + str(width*length))

# Exercise 4
print("Input number a:")
a = float(input())
print("Input number b:")
b = float(input())

if b == 0:
    print("Sum:" + str(a+b))
    print("Product:" + str(a*b))
    print("Difference:" + str(a-b))
    print("Quotient: Can't divide by zero")
else:
    print("Sum: " + str(a + b))
    print("Product: " + str(a * b))
    print("Difference: " + str(a - b))
    print("Quotient: " + str(a/b))

# Exercise 5
print("Input circle's radius:")
R = float(input())
Pi = 3.14159
print("Diameter: " + str(R*2))
print("Circumference: " + str(2*Pi*R))
print("Area: " + str(Pi*R**2))

# Exercise 6
print("Input a number:")
A = int(input())
Sum = 0
Dif = 0
Prod = 0
x = True

# Reversing the number
reversed_n = 0
while A > 0:
    temp = A % 10
    reversed_n = (reversed_n * 10) + temp
    A = A//10

# Main calculations
while reversed_n > 0:
    if reversed_n < 10:
        i = reversed_n
    else:
        i = int(reversed_n % 10)
    Sum += i
    # Checking if it's a first iteration
    if x:
        Dif += i
        Prod += i
        x = False
    else:
        Dif -= i
        Prod *= i
    reversed_n = reversed_n // 10

print("Sum: " + str(Sum))
print("Difference: " + str(Dif))
print("Product: " + str(Prod))
