
name=input()
mystack=[]
for i in name:
    mystack.append(i)

print(mystack)
reverseword=''
while(len(mystack)!=0):
    reverseword=reverseword + mystack.pop()
print(reverseword)
digit = 8

