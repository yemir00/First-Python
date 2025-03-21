numbers=[]

for i in range(6):
    num=int(input(f"Enter Number {i+1}:"))
    numbers.append(num)

numbers[2]=100

print("The New Updated List Is:",numbers)