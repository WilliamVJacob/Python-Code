#program to enter multiple datatypes in a list then arranging them according to there datatypes
l1= [];
l2= [];
l3= [];
l4= [];
l1=[1,2,3,4,'a','b','c','d',1.1,2.2,3.3,4.4]

#l1=['a','b','c','d',1,2,3,1.0,2.0,3.5];
for i in range(0,len(l1)):
	if(type(l1[i])== str):
		num=l1[i];
		l2.append(num);
	elif(type(l1[i])==int):
		num=l1[i];
		l3.append(num);
	elif(type(l1[i])== float):
		num=l1[i];
		l4.append(num);
print (l2,"is string type\n",l3,"is  integer type\n",l4,"is float type\n");	
			
