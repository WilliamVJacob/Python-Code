myList = []
counter = 0 
while counter<10: #change this to true for infinite (unlimited) loop. also remove counter variables
    num = input("Enter numbers or (q)uit")
    myList.append(int(num))
    counter +=1

print (myList) 
