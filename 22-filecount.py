#program to print the number of word, total alphabet and total lines
s="Hello my name is william"
def file2string():
	fp=open("a","r")
	s=fp.read();
	fp.close();
	return s
def countletter(s):
	c=0;d=0;
	for i in range(0,len(s)):
		if(s[i]==' ' or s[i]=='\n'):
			d=d+1;
			if(s[i]=='\n'):
				c=c+1;

	print("the total words are",d,"total alpha are",len(s)-d,"and lines are :",c);
s=file2string()
countletter(s)
