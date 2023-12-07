import math

f = open('data/output.conf', 'r')
k = 0
dots = []
for line in f:
    line.replace("\n", "")
    if k % 4 == 0:
        l = line.split(' ')
        cn = int(l[-1].replace("\n", ""))
        if cn == 2: cn = -1
    elif k % 4 == 3:
        l = line.split(';') 
        for i in range(len(l)-1):
            l1 = l[i][0:-2]
            l2 = l1.split(',')
            if cn == -1:
                l2[0] = float(l2[0]) * (-1)
                l2[1] = float(l2[1]) * (-1)
            dots.append([float(l2[0]), float(l2[1]), int(cn)])
    k += 1

x = []
y = []

for i in range(len(dots)):
    if dots[i][2] == 1:
        x.append([dots[i][0], dots[i][1]])
    else:
        y.append([dots[i][0], dots[i][1]])

def Evklid(x, y):
    dist = []
    for i in range(len(x)):
        dist.append(math.sqrt(sum([(x[i][j] - y[i][j])**2 for j in range(len(x[i]))])))
    return dist

def Manhattan(x, y):
    dist = []
    for i in range(len(x)):
        dist.append(sum([abs(x[i][j] - y[i][j]) for j in range(len(x[i]))]))
    return dist

def Ravnomern(x, y):
    dist = []
    for i in range(len(x)):
        dist.append(max(x[i][j] - y[i][j] for j in range(len(x[i]))))
    return dist

def Minkovsk(x, y):
    dist = []
    for i in range(len(x)):
        dist.append((sum([(x[i][j] - y[i][j])**5 for j in range(len(x[i]))]))**(1/5))
    return dist


print("Evklid Metric")
print(Evklid(x, y))
print("\n")

print("Manhattan Metric")
print(Manhattan(x, y))
print("\n")

print("Ravnomern Metric")
print(Ravnomern(x, y))
print("\n")

print("Minkovsk Metric")
print(Minkovsk(x, y))
print("\n")