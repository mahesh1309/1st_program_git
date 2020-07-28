#File handling
f=open("Mahesh.txt","w")

j=input("Enter some data :")
j1=input()
l=[j,j1]
f.writelines(l)
f.close()

f=open("Mahesh.txt","r")
print(f.read())
f.close()

#for binary file
k=open("1.JPG","rb")
k1=open("govind1.JPG","wb")
for i in k:
    k1.write(i)
k.close()
k1.close()


