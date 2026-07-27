# If Statement

num = int(input("Enter a number: "))
if num % 2 == 0:
    print("Given number is a Even Number")

# -------------------------------------------

# If-else Statement
num = int(input("Enter a number: "))
if num % 2 == 0:
    print("Given number is a Even Number")
else:
    print("Given number is Odd Number")

# ---------------------------------------------


# Looping 

# While Loop
i = 1
while i <= 10:
    print(i, end = " ")
    i+=1

# --------------------------------------------

# For Loop
print("\nString Iteration")

s = "Sanket"
for i in s:
    print(i)

# --------------------------------------------

# While with else

i = 1
while i <= 10:
    print(i, end = " ")
    i+=1
else:
    print("\nEnd of List")
    
# -----------------------------------------

# For with else

tuple = (3,4,6,8,9,2,3,8,9,7)
for value in tuple:
    if value % 2 != 0:
        print(value)
    else:
        print("These are the odd numbers present in the tuple")
print("\n")

# --------------------------------------------

#  for loop with range keyword

x = range(3,6)
for n in x:
    print(n)

print("\n")
# ====================================================

# Branching OR Jumping Statements

# 1) break Statement
for string in "Python Loops" :
    if string == "L":
        break
    print("Current Letters: ", string)
print("\n")
# --------------------------------------------------

# 2) continue statement

for string in "Python Loops":
    if string == "o" or string == "L":
        continue
    print("Current Letters: ", string)
print("\n")
# -----------------------------------------------------

# pass statement

def pass_example():
    for i in range(0,10):
        pass
    print("Good Bye!")
pass_example()
print("\n")


# =========================================

# Sequence program

def sum_of_two_no():
    num1 = 7.2
    num2 = 5.5
    sum = float(num1) + float(num2)
    print("The sum is: ", sum)
sum_of_two_no()