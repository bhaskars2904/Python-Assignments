def Prod(X, Y, n):
   """
    Input: X, Y string of numbers, n an integer denoting number of digits of X or Y
    Output: product of X and Y

   """
   if n==1:
       return int(X)*int(Y)
   else:
       a = X[:n//2]
       b = X[n//2:]
       c = Y[:n//2]
       d = Y[n//2:]       
       p = str(Prod(a, c, n//2))
       q = str(Prod(b, d, n-n//2))
       r = str(int(a)+int(b))
       s = str(int(c)+int(d))
       if len(r)==len(s):
           t = Prod(r, s, len(r))
       elif len(r)>len(s):
           t = Prod(r, (len(r)-len(s))*'0'+s, len(r))
       else:
           t = Prod((len(s)-len(r))*'0'+r, s, len(s))
       u = t-int(p)-int(q)
       if n%2 == 0:
           return int(p+n*'0')+int(str(u)+n//2*'0')+int(q)
       else:
           return int(p+2*(n//2+1)*'0')+int(str(u)+(n//2+1)*'0')+int(q) 
 #Time complexity of above algorithm is O(n^1.6)
print Prod('3141592653589793238462643383279502884197169399375105820974944592', '2718281828459045235360287471352662497757247093699959574966967627', 64)        