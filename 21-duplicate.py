
#program to delete all the repetitive character in a list 
c=0;
lis=[1,2,3,4,5,1,2,3,4,5,1];
lis1=[];
k=0	
for i in range(0,len(lis)):
	for j in range(0,i+1):
		if(lis[j]==lis[i]):
			c=c+1;
			if(c>1):
				break;
	if(c==1):
		lis1.append(lis[i]);
		k+=1;	
	c=0;
		
print(lis1);
