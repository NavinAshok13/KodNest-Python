n=int(input("Enter num"))
number=1
total=0
while number<=n:
    if number%2==0:
        total=total+number
    number=number+1
print("Even Sum: ",total)
