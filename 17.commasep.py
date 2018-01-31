#program to enter number followed by commas and the storing those numbers in a list
arr=[];r=0;
a=input("ENter  numbers followed by commas :")
l=a.split(",")
m=''

for c in a:
	if(c!=','):
		m=m+c;
	else:
	
		arr.append(int(m));
		m='';
	

	
arr.append(int(m));
print(arr);
