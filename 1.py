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

