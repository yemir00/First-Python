numbers=[7, 5, 6, 12, 35, 27]
sum_=0
count=0
average=0

print("The Numbers Are:",end=" ")
for i in range(6):
    print(numbers[i],end=" ")
    sum_+=numbers[i]
    count+=1

average=sum_/count

print(f"\nTheir Sum={sum_}")
print(f"Their Average={average}")