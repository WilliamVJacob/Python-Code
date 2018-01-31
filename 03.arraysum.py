#arr =[1,2,3,4,5];

arr1=[]
v=1
for i in range (5):
	v=input("Enter a no:")
	arr1.append(int(v))
#	i=i+1;
#arr =[2,2,3,4,5];
#print (arr1)
sum=0;
for i in range (0,5):
	sum=sum + arr1[i];
	print (arr1[i])
print (sum);
