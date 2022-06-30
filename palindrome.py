t=int(input())

for i in range(t):
    pal = input()

    l=len(pal)
    decision = 1
    for j in range(0,l//2):
        if (pal[j]!=pal[l-j-1]):
            decision=0

    if(decision == 1):
        print("wins")
    else:
        print("loses")