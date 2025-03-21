ROWS=3
COLS=4

array=[[1,2,3,4],
       [5,6,7,8],
       [9,10,11,12]]

for i in range(ROWS):
    for n in range(COLS):
        print(array[i][n],end=" ")
    print()