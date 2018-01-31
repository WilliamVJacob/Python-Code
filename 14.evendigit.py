#program to find all the numbers between 10 and 999 whose digits are even
#a=int(input("Enter a no :"));

arr=[];
c=0;
for i in range (10,990):
    a=i;
    while (a!=0):
        r=a%10;
        if(r%2!=0):
            c=0;
            break;
        c=1
        a=a//10;
    if(c==1):
        arr.append(i);
    c=0;
print(arr);
    
