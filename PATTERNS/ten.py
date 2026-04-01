n=int(input("enter no of rows"))
for i in range(1,2*n-1):
    if i<=n:
        for j in range(i):
            print("*",end="")
    else:
        for j in range(2*n-i):
            print("*",end="")
    print()

 

        
    

