ROWS=2
COLS=3

array=[[0 for _ in range(COLS)] for _ in range(ROWS)]

for i in range(ROWS):
    for n in range(COLS):
        array[i][n]=int(input(f"Enter Array [{i}][{n}]:"))
    print()

for i in range(ROWS):
    for n in range(COLS):
        print(array[i][n],end=" ")
    print()
