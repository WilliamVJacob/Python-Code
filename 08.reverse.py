#program to find the reverse of the number 
n=int(input("ENter the number"));
rev=0;
while (n!=0):
	r=n%10;
	rev=rev*10 +r;
	n=n//10;
print (rev);
