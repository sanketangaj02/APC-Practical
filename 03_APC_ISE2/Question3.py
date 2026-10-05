# Print a number triangle: 1, 12, 123, etc. 

n = int(input("Enter level of triangle: "))
for i in range(1, n+1):
    for j in range(1, i+1):

        print(j, end=" ")
        
    print()
