marks=int(input("Enter marks: "))
atten=int(input("Enter attendance: "))
pro=input("Enter project completion status (yes/no): ")
if marks>=60 and atten>=75 and pro=="yes":
    print("Eligible")
else:
    print("Not Eligible")
