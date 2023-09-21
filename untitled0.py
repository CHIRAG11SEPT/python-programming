a=int(input())
if (a-1)%2==0:
    print("Weird")
elif a%2==0 and a=="2,3,4,5":
    print("Not Weird")
elif a%2==0 and a=="6,7,8,9,10,11,12,13,14,15,16,17,18,19,20":
    print("Weird")
else:
    print("Not Weird")
