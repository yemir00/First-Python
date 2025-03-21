def print_array(array):
    for i in array:
        print(i,end=" ")
    print()

array=[-2, 45, 0, 11, -9]
size=len(array)

for i in range(1,size):
    for n in range(size-i):
        if array[n]>array[n+1]:
            array[n],array[n+1]=array[n+1],array[n]

print("Sorted Array in Ascending Order:",end=" ")
print_array(array)