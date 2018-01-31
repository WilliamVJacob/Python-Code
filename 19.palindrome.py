a=input("Enter a string");
j=len(a)-1;
out='a';
b=''
for i in range(0,len(a)):
	b=b+a[j];
#	print(a[j],"$$ ");
	j=j-1;
if(a==b):
	print("palindrome");
else:
	print("not palindrome");
#print(b)
