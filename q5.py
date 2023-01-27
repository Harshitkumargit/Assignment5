rows=int(input("enter number of rows"))
count=0
for i in range(rows+1):
    for j in range(i):
        if count>=26:
            count=0
        print(chr(65+count),end="")
        count+=1
    print()
