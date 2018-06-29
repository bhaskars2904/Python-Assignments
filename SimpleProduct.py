from __future__ import print_function
l = [0]*1
l[0] = 0
flag=0
def frag(s):
    """
    input: s, an int
    Returns a list x, an ordered pair of tens and units digit of s
    """
    x = [0]*2
    x[1]=s%10
    x[0]=s//10
    return x

a = raw_input("Enter a ")
b = raw_input("Enter b ")
for i in range (len(a)-1,-1,-1):
    k = len (a)-i-1
    carry = 0
    for j in range(len(b)-1,-1,-1):
        p = int(a[i])*int(b[j])
        if k+1>len(l):
            add = p+carry
            v = frag(add)
            carry = int(v[0])
            l.append(int(v[1]))
        else:
            add = p+carry+l[k]
            v = frag(add)
            carry = int(v[0])
            l[k] = int(v[1])
        if j==0:
            l.append(carry)
        k += 1
l.reverse()
print ("\nProduct of supplied input numbers = ", end="")
for i in range(len(l)):
    if l[i]!=0:
        flag=1
    if flag==1:
        print (l[i], end=""),