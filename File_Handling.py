# 1) Write a Python program to create a file named student.txt and write the student's name, roll number, branch, and semester into the file. 

file = open("student.txt", "w")

file.write("Name: Sanket Angaj\n")
file.write("Roll Number: 03\n")
file.write("Branch: Computer Science and Engineering\n")
file.write("Semester: V\n")

file.close()

print("Student details written successfully.")


# 2) Write a program to open a text file and display its complete contents.

file = open("student.txt", "r")

content = file.read()

print(content)
file.close()


# 3) Write a program to append additional student information to an existing file without deleting its previous contents.

file = open("student.txt", "a")

file.write("\nName: Chetan Patil\n")
file.write("Roll Number: 123\n")
file.write("Branch: Civil Engineering\n")
file.write("Semester: V\n")

file.close()

print("Additional student information added successfully.")


# 4) Write a program to read a text file line by line and display each line separately.

with open("student.txt", "r") as file:

    for line in file:
        print(line, end="")


# 5) Write a program to count and display the total number of lines present in a text file. 

with open("student.txt", "r") as file:

    count = 0

    for line in file:
        count += 1

print("Total number of lines:", count)


# 6) Write a program to count the total number of words present in a text file. 

with open("student.txt", "r") as file:

    content = file.read()

    words = content.split()

    count = len(words)

print("Total Number of Words:", count)