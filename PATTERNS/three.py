rows=int(input("eter no of rows"))
for i in range(1,rows+1):
    for j in range(1,i+1):
        print(j,end="")
    print()

#timecomplexity -O(n^2)
#spacecomplexity-O(1)