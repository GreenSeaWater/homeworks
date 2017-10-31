def swap_case(s):
    newString = ""
    for i in s:
        if i.isupper():
            newString += i.lower()
        else:
            newString += i.upper()
            
    return newString