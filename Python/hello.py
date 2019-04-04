#f=open('test.dat','w')
#f.write('How are you')
#f.write('121')
#f.close()
#f=open('test.dat','r')
#print (f.read())
#f.close()

#import pickle
#n=input("enter the limit :")
#f1=open("test.dat","w")
#for i in range(n):
#    r=input("enter the number :")
#    pickle.dump(r,f1)
#f1.close()#
#f1=open("test.dat","r")
#for i in range(n):
#    print(pickle.load(f1))

#login using password in file
fodj=open("login3.txt","w")
fodj.write("ictak\n")
fodj.close()
fodj=open("login3.txt","a")
fodj.write("1234")
username=input("enter username :")
password=input("Enter password :")
fodj=open("login3.txt","r")
uname=fodj.readline()
passs=fodj.readline()
print(username)
print(password)
print(uname)
print(passs)
uname=uname.rstrip("\n")
if username==uname and password==passs:
    print("login successful")
else:
    print("login Unsuccessful")