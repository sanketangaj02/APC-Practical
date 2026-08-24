# 1. Write a function factorial(n) that accepts an integer and returns its factorial.

def factorial(n):
    fact = 1

    for i in range(1, n + 1):
        fact = fact * i

    return fact

n = int(input("Enter a number: "))
print("Factorial =", factorial(n))


# 2. Write a function check_even_odd(n) that determines whether a given number is even or odd.

def check_even_odd(n):
    if n % 2 == 0:
        return "Even"
    else:
        return "Odd"


n = int(input("Enter a number: "))
print(check_even_odd(n))


# 3. Define a function that accepts two numbers and returns the greater number.

def greater(a, b):
    if a > b:
        return a
    else:
        return b

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

result = greater(num1, num2)
print("Greater number is:", result)


# 4. Create a function simple_interest(p, r, t) to calculate simple interest.

def simple_interest(p, r, t):
    si = (p * r * t) / 100
    return si

p = float(input("Enter principal amount: "))
r = float(input("Enter rate of interest: "))
t = float(input("Enter time(year(s)): "))

result = simple_interest(p, r, t)

print("Simple Interest =", result)