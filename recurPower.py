def recurPower(base, exp):
    """
    
    input: base, an int or float. exp, an int
    
    output: Returns the value of base^exp
    
    
    """
    if exp==0:
        return 1
    else:
        if exp%2 == 0:
            ans = recurPower(base, exp/2)
            return ans*ans
        else:
            ans = recurPower(base, exp//2)
            return ans*ans*base
 