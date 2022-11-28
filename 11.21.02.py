name = ["john","marry","tom","amy"]
subject = ["math","language","python"]
avg = list()

for i in name:
    print("student:",i)
    sum = 0
    for j in subject:
        prompt = "**enter " + j + " score:"
        score = eval(input(prompt))
        sum+=score
    avg.append(sum/3)

print("===RESULT:===")
for i in range(len(name)):
    print(name[i]," avg is ",round(avg[i],1))

#找最大
max = avg[0]
ind = 0
for i in range(len(avg)):
    if max < avg[i]:
        max = avg[i]
        ind = i
print("the highest on is",name[ind],"average is ",avg[ind])
