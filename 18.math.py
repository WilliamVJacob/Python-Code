import math
#a=input("Enter a number followed by commas");
a="100,150,180"
c=50;h=30;
arr=[];
arr1=[]
d=a.split(",");
arr.append(d);
#arr1=int(arr);
print (arr)
i=0;
for d in a:
    
    r=arr[0];
    
    e=math.sqrt(2*c*float(d/h))
    print(e)
    i=i+1;
    #arr.append(str(int(round())))))
#print (arr)
