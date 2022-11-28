def ctof(x):
    return x*1.8+32

def ftoc(x):
    return (x-32)*5/9

def CF(type,x):
    if type.upper()=="C":
        return ctof(x)
    else:
        return ftoc(x)
