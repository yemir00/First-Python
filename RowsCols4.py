rows=int(input("Enter the number of rows:"))
cols=int(input("Enter the number of cols:"))

array=[[0 for _ in range(cols)] for _ in range(rows)]

for i in range(rows):
    for n in range(cols):
        array[i][n]=int(input(f"Enter Array [{i}][{n}]: "))
    print()

for i in range(rows):
    for n in range(cols):
        print(array[i][n],end=" ")
    print()