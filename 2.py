print("11144155 鐘子傑")

def multTable(n):
    for a in range(2,n+1):
        for b in range(1,n+1):
            print(a,"*",b,"=",a*b,end="\t")
        else:
            print()

print("第一題_1:")
multTable(9)
print("第二題_2:")
multTable(5)


def big(n):
    a = 1
    b = 0
    if b > n:
        b = a*a
        print(a)
    else:
        a = a+1

big(300)        































