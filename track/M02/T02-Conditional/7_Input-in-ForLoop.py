n=int(input("Enter N: "))
pos=0
neg=0
z=0
t=0
for i in range(1,n+1):
    s=int(input("Enter number: "))
    t=t+s
    if s>0:
        pos+=1
    elif s<0:
        neg+=1
    else:
        z+=1
print("Positive Count:",pos)
print("Negative Count:",neg)
print("Zero Count:",z)
print("Total:",t)