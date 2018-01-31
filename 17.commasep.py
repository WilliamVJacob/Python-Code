arr=[];r=0;
a=input("ENter a number followed by commas :")
l=a.split(",")
m=''

for c in a:
#	r=r*10+int(c);	
	
	#print(a[5]);	
	if(c!=','):
		m=m+c;
		#continue
	else:
	
		arr.append(int(m));
		m='';
	

	
#print (m)
#arr.append(l);
arr.append(int(m));
print(arr);
