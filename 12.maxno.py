l1=[ 5,4,43,2,1];
i=0;
big=l1[0];

for i in range(0,len(l1)):
   if(big < l1[i]):
       big=l1[i];

print (big,"is the max value");
