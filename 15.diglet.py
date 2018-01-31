a=input("Enter alphanumeric character :");
digit=0;
letter=0;
spc=0;
for c in a:
    if (c.isdigit()):
        digit=digit+1;
    elif (c.isalpha()):
        letter=letter+1;
    else:
        spc=spc+1;
print ("total digit is ",digit," and total letter is ",letter,"the special character are",spc);
