mat1=[0,0],[0,0]
mat2=[0,0],[0,0]
sum_mat=[0,0],[0,0]

print("Inters the values of the matrix: ")

for i in range(2):
    for n in range(2):
        mat1[i][n]=int(input(f"Enter value of mat1 [{i}][{n}]:"))

for i in range(2):
    for n in range(2):
        mat2[i][n]=int(input(f"Enter value for mat2 [{i}][{n}]:"))

for i in range(2):
    for n in range(2):
        sum_mat[i][n]=mat1[i][n]+mat2[i][n]

for i in range(2):
    for n in range(2):
        print(sum_mat[i][n],end=" ")
    print()