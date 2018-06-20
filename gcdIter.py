def gcdIter(a, b):
    """
    
    input: a, b, two positive integers
    
    output: Returns gcd of a, b
    
    
    """
    low = 1
    if a<b:
        low = a
    else:
        low = b
    for i in range (low,0,-1):
        if a%i == 0 and b%i == 0:
            break
    return i
