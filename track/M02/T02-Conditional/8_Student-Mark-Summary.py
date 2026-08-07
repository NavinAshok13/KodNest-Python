s=int(input())
total=0
passed=0
fail=0
i=1
while i<=s:
    mark=int(input())
    total+=mark
    if mark>=40:
        passed+=1
    else:
        fail+=1
    i+=1
print("Total Marks:",total)
print("Passed Students:",passed)
print("Failed Students:",fail)
if fail==0:
    print("Batch Result: All Passed")
else:
    print("Batch Result: Needs Improvement")