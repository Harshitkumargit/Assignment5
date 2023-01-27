list1=[]
for i in range(1,501):
    if i%7==0 and i%5==0:
        list1.append(i)
l=len(list1)
for j in range(l):
    print(list1[j])
