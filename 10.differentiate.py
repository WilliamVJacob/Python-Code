#a=input("ENter a no:");
l1= [];
l2= [];
l3= [];
l4= [];
while 1: #change this to true for infinite (unlimited) loop. also remove counter variables
	num = input("Enter numbers or (q)uit");
	l1.append(num)
	if(num=='q'):
		break;


#l1=['a','b','c','d',1,2,3,1.0,2.0,3.5];
for i in range(0,len(l1)):
	if(type(l1[i])== str):
		num=l1[i];
		l2.append(num);
		print(l1[i]);
	elif(type(l1[i])==int):
		num=l1[i];
		l3.append(num);
	elif(type(l1[i])== float):
		num=l1[i];
		l4.append(num);
print (l2,"is string type\n",l3,"is  integer type\n",l4,"is float type\n");	
			
#print(len(l1));
#if(type(a)==str):
#	c=1;
#else:
#	c=0;
#print (c);
