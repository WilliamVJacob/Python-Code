#num=int(input("ENter a no:"));
c=0;sum1=0;
for j in range(2,101):
	for i in range(2,j):
		if(j%i==0):
			c=1;
		#	print ("Not prime");
			break;
	
	if(c==0):
		print (j);
		sum1=sum1+j;
	c=0;
print(sum1);






