rows=int(input("enter no of rows"))
for i in range(1,rows+1):
    for j in range(rows-i+1):
        print("*",end="")
    print()

    #timecomplexity -O(n^2)
#spacecomplexity-O(1)

