number=int(input("enter a number:"))
n=int(input("enter the range:"))
for i in range(1,n+1):
    if number%i==0:
        print(i)
