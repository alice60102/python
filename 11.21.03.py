arr = [[1,2,3],[4,5,6],[7,8,9]]
print("Item1\tItem2\tItem3\tSum")
for i in range(len(arr)):
    rsum = 0
    for j in range(len(arr[i])):
        print(arr[i][j], end="\t")
        rsum += arr[i][j]
    print(rsum)

print(35*'=')

for i in range(len(arr)):
    csum = 0
    for j in range(len(arr[i])):
        csum += arr[j][i]
    print(csum, end ="\t")
