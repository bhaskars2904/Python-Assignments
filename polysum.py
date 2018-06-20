import math
def polysum(n, s):
    """
    
    input: n, an int and s, an int or float
    
    output: Returns the sum of area of a polygon with n sides having length s each, and square of its perimeter
    
    
    """
    area = (0.25*n*s*s)/math.tan(math.pi/n)
    perimeter = n*s
    sum = area + perimeter*perimeter
    return round(sum, 4)
