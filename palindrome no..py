num= int ( input())
c=num
s=0
while num != 0:
    r = num % 10
    s= s * 10 + r
    num = num // 10
print('reverse of',c,'is',s)

if c == s:
    print("number is palindrome")
else:
    print("number is not palindrome")