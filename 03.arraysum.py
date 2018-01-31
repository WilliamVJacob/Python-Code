#program to print the sum of all the elements in the list
arr1=[]
v=1
for i in range (5):
	v=input("Enter a no:")
	arr1.append(int(v))
sum=0;
for i in range (0,5):
	sum=sum + arr1[i];
	print (arr1[i])
print (sum);
