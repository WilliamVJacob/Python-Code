#lis=[1,2,3,4,5,1,2,3,4,5,1];
lis=[1,2,1,4];
c=0;
j=0	
#d=lis[j];
#lis.remove(1);

for i in range(0,len(lis)):
	for j in range(0,len(lis)):
		if(lis[i]==lis[j]):
			c=c+1;
			if(c>1):
				print(lis[j],lis[i],c);	
#				lis.remove(lis[i]);

		
	c=0;
		
print(lis);
