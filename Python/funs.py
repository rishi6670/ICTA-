#Functions
#def sum(a,b):
#    x=a+b
#    return x
#a=input("enterthe number :")
#b=input("enter the number :")
#print sum(a,b)

 #Rcursion
#def factorial(n):
#    if n==0:
#        return 1
#    else:
#        return n*factorial(n-1)
#n=int(input("Enter number :"))
#print factorial(n)

# calculator

def sum(x,y):
    z=x+y
    return z
def sub(x,y):
    z=x-y
    return z
def mul(x,y):
    z=x*y
    return z
def divi(x,y):
    z=x/y
    return z


ch=0
if ch!=5:
    print "1.Addition"
    print "2.Subtraction"
    print "3.Multiplication"
    print "4 .Division"
    print "5.Exit"
    print" "
    ch=int(input("enter your choice :"))
    if ch==1:
        a=int(input("Enter the first no :"))
        b=int(input("Enter the second no:"))
        print sum(a,b)
    elif ch==2:
        a=int(input("Enter the first no :"))
        b=int(input("Enter the second no:"))
        print sub(a,b)
    elif ch==3:
        a=int(input("Enter the first no :"))
        b=int(input("Enter the second no:"))
        print mul(a,b)
    elif ch==4:
        a=int(input("Enter the first no :"))
        b=int(input("Enter the second no:"))
        print divi(a,b)
    elif ch==5:
        print "Thank You"
    else:
        print "Invalid Choice"
else:
    exit
