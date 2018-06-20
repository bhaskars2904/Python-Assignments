def iterPower(base, exp):
    """
    
    input: base, an int or float. exp, an int
    
    ouput: Returns the value of base^exp
    
    
    """
    ans = 1
    if exp%2 == 0:
        for i in range(exp/2):
            ans = ans*base
        return ans*ans
    else:
        for i in range(exp//2):
            ans = ans*base
        return ans*ans*base

