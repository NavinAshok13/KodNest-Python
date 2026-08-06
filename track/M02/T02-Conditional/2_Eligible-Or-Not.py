marks=int(input("Enter marks: "))
atten=int(input("Enter attendance: "))
pro=input("Enter project completion status (yes/no): ").lower()
if marks>=60:
     if atten>=75:
        if pro=="yes":
            print("Eligible")
else:
    print("Not Eligible")
