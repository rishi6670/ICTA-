#a = [1,"hello",3.5,[2,"welcome",4.5]]

#print a

#print a[1]

#for i in a:
#    print i

#a[0]=2
#print a[0]

#a[3][1]="hai"
#print a[3][1]

#a=[1,2,3]
#b=a+[1]
#print b
#c=b*3
#print c

#a=[1,2,3]
#a.append(4) #to add an element in last position 
#print a

#a=[1,2,3]
#b=[4,5,6]
#a.extend(b) #to add second list to the first list
#print a

#a=[0,1,2,3]
#a.insert(1,2) #insert a value into list (index,value)
#print a

#a=[0,1,2,3]
#a.pop()  #to delete last element from list
#print a

#a=[0,1,2,3]
#a.pop(0) # to delete an element from list pop(index)
#print a

#a=[0,1,2,3]
#print a[::-1] # to reverse a list
#a.reverse()
#print a

# to find largest and smallest no in list
#maz=0
#a=[1,2,3,4,5,5,6,6,7]
#for i in a:
#    if i>maz:
#        maz=i
#    if i<min:
#        min=i
#print "large :",maz,"small :",min

# list index
#lst=[]
#num=int(input("How many numbers :"))
#for n in range(num):
#    numbers=int(input("Enter the number :"))
#    lst.append(numbers)
#print lst    
#print max(lst)
#print min(lst)

#dictionary

#b={"welcome":"come",3.5:"three point five",4:"four"}
#print b
#b[welcome]="comewel"
#print b[welcome]
#print b.keys()
#print b.values()
#print b.items()
#for i in b:
 #   print i,b[i]

#print b.has_key("welcome")
#print b.get("welcome")
#del b[4]
#print b
 
 #home work Q1
#b=["circle","square","triangle"]
#b[0]="elipse"
#print b
#b.insert(0,"rectangle") #add an element to first position
#print b
#b.pop(3)
#print b

#homework Q2
farm={"sheep":5,"cow":2,"goats":10}
#print farm
farm.update({"duck":8}) #to update a new key and value to dictionary
#print farm
print len(farm)  #to display no of items in dictionary