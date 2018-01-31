l1=[ 5,4,3,2,1];
i=0;
for j in range (0,len(l1)):
    for i in range(0,len(l1)):
        if(l1[i] > l1[j]):
            temp=l1[i];
            l1[i]=l1[j];
            l1[j]=temp;
print (l1);
