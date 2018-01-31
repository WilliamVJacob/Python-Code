

v1=int(input("ENter the 1st No:"));
v2=int(input("ENter the 2nd No:"));
v3=int(input("ENter the 3rd No:"));
if(v1>v2):
	if(v1>v3):
		max1=v1;
	else:	
		max1=v3;
else:
	max1=v2;
print(max1,"is the maximum value");
