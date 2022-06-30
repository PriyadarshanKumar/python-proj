arr=[65, 2, 34, 3, 21, 1, 5, 22]

for i in range(1, len(arr)):
    temp=arr[i]
    print(temp)
    for j in range(i-1,-1,-1):

        if(arr[j]>temp):
            # j-=1
            arr[j + 1]=arr[j]
        else:
            j+=1
            break
        print(arr)

    arr[j]= temp
    print(arr)
print(arr)

