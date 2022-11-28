def draw(n,s):
    return print(s*n)

def arithmetic(a,b,type):
    if type.upper()=="ADDITION":
        return print(a,"",b,"","ADDITION","=",(a+b))
    elif type.upper()=="SUBTRACTION":
        return print(a,"",b,"","SUBTRACTION","=",(a-b))
    elif type.upper()=="MULTIPLICATION":
        return print(a,"",b,"","MULTIPLICATION","=",(a*b))
    elif type.upper()=="DIVISION":
         return print(a,"",b,"","DIVISION","=",(a/b))
    else:
        return "wrong"

def digitTower(c):
    for x in range(1,c+2):
        for y in range(1,x):
            print(y,end="")
        else:
            print()



draw("=",10)

arithmetic(10,2,"ADDITION")

draw("=",10)

arithmetic(10,2,"SUBTRACTION")

draw("=",10)

arithmetic(10,2,"MULTIPLICATION")

draw("=",10)

arithmetic(10,2,"DIVISION")

draw("=",10)

draw("*",10)

digitTower(9)

draw("*",10)







