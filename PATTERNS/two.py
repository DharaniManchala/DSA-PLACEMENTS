rows=int(input("enter no of rows:"))

for i in range(rows):
    for j in range(i):
        print("*",end="")
    print()



#timecomplexity -O(n^2)
#spacecomplexity-O(1)