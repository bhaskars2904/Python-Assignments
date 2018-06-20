def isIn(char, aStr):
    """
    
    input: char, a character and aStr, an input string in alphabetical order
    
    output: Returns True if character is conatined in string, false otherwise
    
    
    """
    if len(aStr) == 0:
        return False
    if len(aStr) == 1:
        return char == aStr
    else:
        if char == aStr[len(aStr)//2]:
            return True
        if char > aStr[len(aStr)//2]:
            return isIn(char, aStr[len(aStr)//2+1:len(aStr)])
        else:
            return isIn(char, aStr[0:len(aStr)//2])
                