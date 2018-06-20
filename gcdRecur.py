def gcdRecur(a, b):
    """
    
    input: a, b, two positive integers
    
    output: Returns gcd of a,b
    
    
    """
    if b == 0:
        return a
    else: 
        return gcdRecur(b, a%b)
