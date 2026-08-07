n = int(input())
scores = []
for i in range(n):
    a=int(input())
    scores.append(a)
search_score = int(input())
high=scores[0]
low=scores[0]
total=0
found=False
for i in range(len(scores)):
    if scores[i] >high:
        high=scores[i]
    if scores[i]<low:
        low=scores[i]
    total=total+scores[i]
    if scores[i]==search_score:
        found=True
print("Highest Score:",high)
print("Lowest Score:",low)
print("Total Score:",total)
if found:
    print("Search Result: Found")
else:
    print("Search Result: Not Found")
    