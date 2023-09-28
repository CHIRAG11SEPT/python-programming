num= int ( input())
cp= num
pw=0

while num != 0:
    pw+= 1
    num = num // 10

s=0
num = cp

while num != 0:
    r = num % 10
    s= s+r** pw
    num = num // 10

if s==cp:
    print("number is armstrong")
else:
    print ("number is not a armstrong")