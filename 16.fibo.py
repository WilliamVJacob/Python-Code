#program to print the first 10 fibonacii numbers
p=0;
c=1;
for i in range (0,10):
    n=p+c;
    print (p);
    p=c;
    c=n;
