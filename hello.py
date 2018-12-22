print("hello git")
sum  = 0
for i in range(1, 100):
    sum += i 
print("e====no sum")

for row in range(1, 10):
    for col in range(1, row+1):
        print(row,"*",col,"=",(row*col),end="\t")
    print()
