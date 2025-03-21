numbers=[0]*5

print("Enter 5 Numbers")

for i in range(5):
    numbers[i]=int(input(f"Enter Number {i+1}:"))

print("The Numbers Are: ",end=" ")

for i in range(5):
    print(numbers[i],end=" ")