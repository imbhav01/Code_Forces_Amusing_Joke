x = str(input())
x1 = []
for i in range(0,len(x)):
    x1.append(x[i])

y = str(input())
y1 = []
for i in range(0,len(y)):
    y1.append(y[i])

a=x1+y1
b = sorted(list(a))


z = str(input())
z1 = []
for i in range(0,len(z)):
    z1.append(z[i])
c = sorted(list(z1))

if b==c:
    print("YES")
else:
    print("NO")